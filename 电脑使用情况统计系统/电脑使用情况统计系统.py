import win32api,win32gui,win32con,win32process,win32console
import ctypes
import time
import threading
import os

def GetForegroundInfo():
    """获取前台窗口信息"""
    #[进程路径,窗口标题,时长]
    last_time=int(time.time())
    last_hwnd=me_hwnd #窗口句柄
    last_text=win32gui.GetWindowText(last_hwnd) #窗口标题
    _,last_pid=win32process.GetWindowThreadProcessId(last_hwnd) #进程标识符
    last_handle=win32api.OpenProcess(win32con.PROCESS_ALL_ACCESS,False,last_pid) #进程句柄
    last_path=win32process.GetModuleFileNameEx(last_handle,0) #进程路径
    while True:
        hwnd=win32gui.GetForegroundWindow() #窗口句柄
        text=win32gui.GetWindowText(hwnd) #窗口标题
        _,pid=win32process.GetWindowThreadProcessId(hwnd) #进程标识符
        handle=win32api.OpenProcess(win32con.PROCESS_ALL_ACCESS,False,pid) #进程句柄
        path=win32process.GetModuleFileNameEx(handle,0) #进程路径
        if text != last_text or path !=last_path:
            now_time=int(time.time())
            now_tuple=(path,text)
            if now_tuple in datadict:
                datadict.update({now_tuple:datadict[now_tuple]+(now_time-last_time)})
            else:
                datadict.update({now_tuple:now_time-last_time})
            file=open('data.txt','wb')
            file.write(str(datadict).encode("utf-8"))
            file.close()
            file=open('log.txt','ab+')
            file.write(str(time.strftime("%H:%M:%S", time.localtime(last_time))+"-"+time.strftime("%H:%M:%S", time.localtime(now_time))+" : "+last_text+" "+last_path+" 用时:"+str(now_time-last_time)+"s\n").encode("utf-8"))
            file.close()
            last_text=text
            last_path=path
            last_time=now_time
        '''
         print(hwnd)
         print(text)
         print(pid)
         print(handle)
         print(path)
        '''
        time.sleep(1)

def HotKeyShowWindow():
    """检测热键以显示窗口"""
    while True:
        if win32api.GetAsyncKeyState(win32con.VK_LCONTROL) and win32api.GetAsyncKeyState(win32con.VK_F10):
            win32gui.ShowWindow(me_hwnd,win32con.SW_SHOW)
            break
        time.sleep(0.1)

#获取自身窗口句柄
me_hwnd=win32console.GetConsoleWindow()
#禁用关闭按钮
close_button=win32gui.GetSystemMenu(me_hwnd,0)
win32gui.RemoveMenu(close_button,win32con.SC_CLOSE,win32con.MF_REMOVE)
#更改窗口标题
win32gui.SetWindowText(me_hwnd,"电脑使用情况统计系统")
#判断本地是否存在统计文件,不存在则创建
isDataExists=os.path.exists('data.txt')
datadict={}
if(isDataExists):
    file=open('data.txt','rb')
    datadict=eval(file.read())
    file.close()
else:
    file=open('data.txt','wb')
    file.write(str(datadict).encode("utf-8"))
    file.close()
#判断本地是否存在日志文件,不存在则创建
isLogExists=os.path.exists('log.txt')
if(not isLogExists):
    file=open('log.txt','wb')
    file.write("".encode("utf-8"))
    file.close()
#开启子线程获取窗口信息
t_getinfo=threading._start_new_thread(GetForegroundInfo)
#输出提示信息
print("——————基于Python的电脑使用情况统计系统——————")
print("当前时间:"+time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))
print("系统已开始运行,输入'help'可获取命令列表")
#控制台主循环
while True:
    cmd=input(">")
    if cmd =='help':
        print("help - 命令列表")
        print("hide - 隐藏窗口(Ctrl+F10重新显示)")
        print("q - 退出系统")
    elif cmd=='hide':
        t_showwindow=threading._start_new_thread(HotKeyShowWindow)
        win32gui.ShowWindow(me_hwnd,win32con.SW_HIDE)
    elif cmd=='q':
        
        break

#win32process.TerminateProcess(handle,1)
#ctypes.windll.user32.LockWorkStation()

'''
flag=True
alpha=255
alphanum=0
while True:
    win32gui.SetWindowLong(hwnd,win32con.GWL_EXSTYLE,win32con.WS_EX_LAYERED)
    win32gui.SetLayeredWindowAttributes(hwnd,0,alpha,win32con.LWA_ALPHA)
    time.sleep(0.001)
    if flag:
        alpha=alpha-1
        if alpha==100:
            flag=bool(1-flag)
            alphanum=alphanum+1
    else:
        alpha=alpha+1
        if alpha==255:
            flag=bool(1-flag)
            alphanum=alphanum+1
            if alphanum==6:
                break
'''

'''
rect=win32gui.GetWindowRect(hwnd)
print(rect)
round=list(rect)
if rect[2]-rect[0]>=rect[3]-rect[1]: #横长方形
    round[1]=round[1]-((rect[2]-rect[0])-(rect[3]-rect[1]))/2
    round[3]=round[3]+((rect[2]-rect[0])-(rect[3]-rect[1]))/2
else: #竖长方形
    pass
for i in range(rect[3]-rect[1]-200):
    test=list(rect)
    #win32gui.SetWindowRgn(hwnd,ctypes.windll.gdi32.CreateEllipticRgn(round[0],round[1],round[2],round[3]),True)
    win32gui.SetWindowRgn(hwnd,win32gui.CreateRoundRectRgn(test[0],test[1],test[2],test[3],200,300),True)
    test[0]=test[0]-1
    test[1]=test[1]-1
    test[2]=test[2]-1
    test[3]=test[3]-1
    time.sleep(0.1)
#win32gui.SetWindowPos(hwnd,0,rect[0]+100,rect[1]+100,rect[2],rect[3],win32con.SWP_NOZORDER)
'''