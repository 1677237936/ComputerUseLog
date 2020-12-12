from tkinter import *
from tkinter import ttk

def ShowSheetDataGUI(DataDict):
    #初始化
    top = Tk()
    #窗口标题
    top.title('数据汇总 - 基于Python的电脑使用情况统计系统')
    #加载窗口图标
    top.iconbitmap("Images/Icon.ico")
    # 窗口居中
    ws = top.winfo_screenwidth()
    hs = top.winfo_screenheight()
    x = (ws / 2) - (1100 / 2)
    y = (hs / 2) - (600 / 2)
    top.geometry('%dx%d+%d+%d' % (1100,600,x,y))

    #表格
    columns = ("时长(秒)", "窗口标题", "进程路径")
    treeview = ttk.Treeview(top, height=18, show="headings", columns=columns)  
    #表示列,不显示
    treeview.column("时长(秒)", width=100, anchor='center') 
    treeview.column("窗口标题", width=500, anchor='center')
    treeview.column("进程路径", width=500, anchor='center')
    #显示表头
    treeview.heading("时长(秒)", text="时长(秒)") 
    treeview.heading("窗口标题", text="窗口标题")
    treeview.heading("进程路径", text="进程路径")
    #添加进窗体
    treeview.pack(side=LEFT, fill=BOTH)
    #添加数据
    SheetDict=DataDict.copy()
    ZippedDict=zip(SheetDict.values(),SheetDict.keys())
    SortedDataList=list(sorted(ZippedDict,key=lambda s: s[0], reverse=True))
    count=1
    for i in SortedDataList:
        treeview.insert("",count,values=(i[0],i[1][1],i[1][0]))
        count=count+1
    #运行
    top.mainloop()
    top.quit()
