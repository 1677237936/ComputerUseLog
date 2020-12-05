import win32api,win32gui,win32con
import ctypes
from GUICallBack import GetForegroundInfo

lpPrevWndProc=0
msgShellHook=0

def StartHook(Hwnd):
    """开始窗口消息钩子"""
    global lpPrevWndProc,msgShellHook
    msgShellHook=win32api.RegisterWindowMessage("SHELLHOOK")
    ctypes.windll.user32.RegisterShellHookWindow(Hwnd)
    lpPrevWndProc=win32gui.SetWindowLong(Hwnd,win32con.GWL_WNDPROC,WindowProc)

def EndHook(Hwnd):
    """结束窗口消息钩子"""
    #还原系统消息处理
    win32api.SetWindowLong(Hwnd,win32con.GWL_WNDPROC,lpPrevWndProc)

def WindowProc(Hwnd,uMsg,wParam,lParam):
    if uMsg==msgShellHook:
        if wParam==1: #HSHELL_WINDOWCREATED
            pass
            #print("HSHELL_WINDOWCREATED")
        elif wParam==2: #HSHELL_WINDOWDESTROYED
            pass
            #print("HSHELL_WINDOWDESTROYED")
        elif wParam==3: #HSHELL_ACTIVATESHELLWINDOW
            pass
        elif wParam==4: #HSHELL_WINDOWACTIVATED
            pass
        elif wParam==5: #HSHELL_GETMINRECT
            pass
        elif wParam==6: #HSHELL_REDRAW
            GetForegroundInfo()
            #print("HSHELL_REDRAW")
        elif wParam==7: #HSHELL_TASKMAN
            pass
        elif wParam==8: #HSHELL_LANGUAGE
            pass
        elif wParam==32772: #ACTIVATE
            GetForegroundInfo()
            #print("ACTIVATE")
        else:
            pass
    return win32gui.CallWindowProc(lpPrevWndProc,Hwnd,uMsg,wParam,lParam)