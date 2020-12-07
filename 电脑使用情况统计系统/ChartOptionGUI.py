import os, sys
from tkinter import *
from tkinter.font import Font
from tkinter.ttk import *
from tkinter.messagebox import *
#import tkinter.filedialog as tkFileDialog
#import tkinter.simpledialog as tkSimpleDialog    #askstring()

class ChartOption_ui(Frame):
    #这个类仅实现界面生成功能，具体事件处理代码在子类ChartOption_callback中。
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.master.title('绘图选项 - 基于Python的电脑使用情况统计系统')
        self.master.resizable(0,0)
        # 窗口居中
        ws = self.master.winfo_screenwidth()
        hs = self.master.winfo_screenheight()
        x = (ws / 2) - (426 / 2)
        y = (hs / 2) - (146 / 2)
        self.master.geometry('%dx%d+%d+%d' % (426,146,x,y))
        self.createWidgets()

    def createWidgets(self):
        self.top = self.winfo_toplevel()

        self.style = Style()

        self.style.configure('TFrameMain.TLabelframe', background='#FFE0C0', font=('微软雅黑',12))
        self.style.configure('TFrameMain.TLabelframe.Label', background='#FFE0C0', font=('微软雅黑',12))
        self.FrameMain = LabelFrame(self.top, text='绘图选项', style='TFrameMain.TLabelframe')
        self.FrameMain.place(relx=0., rely=0., relwidth=0.998, relheight=0.993)

        self.CmdSubmitVar = StringVar(value=' 生成！')
        self.style.configure('TCmdSubmit.TButton', background='#FFC0C0', font=('微软雅黑',12))
        self.CmdSubmit = Button(self.FrameMain, text=' 生成！', textvariable=self.CmdSubmitVar, command=self.CmdSubmit_Cmd, style='TCmdSubmit.TButton')
        self.CmdSubmit.setText = lambda x: self.CmdSubmitVar.set(x)
        self.CmdSubmit.text = lambda : self.CmdSubmitVar.get()
        self.CmdSubmit.place(relx=0.645, rely=0.593, relwidth=0.196, relheight=0.240)

        self.ComboFilterList = ['前10','前20','前30']
        self.ComboFilterVar = StringVar(value='前10')
        self.ComboFilter = Combobox(self.FrameMain, state='readonly', text='前10', textvariable=self.ComboFilterVar, values=self.ComboFilterList, font=('微软雅黑',10))
        self.ComboFilter.setText = lambda x: self.ComboFilterVar.set(x)
        self.ComboFilter.text = lambda : self.ComboFilterVar.get()
        self.ComboFilter.place(relx=0.650, rely=0.173, relwidth=0.267)

        self.ComboViewList = ['日视图','周视图','月视图','总视图']
        self.ComboViewVar = StringVar(value='日视图')
        self.ComboView = Combobox(self.FrameMain, state='readonly', text='日视图', textvariable=self.ComboViewVar, values=self.ComboViewList, font=('微软雅黑',10))
        self.ComboView.setText = lambda x: self.ComboViewVar.set(x)
        self.ComboView.text = lambda : self.ComboViewVar.get()
        self.ComboView.place(relx=0.196, rely=0.586, relwidth=0.267)

        self.ComboTypeList = ['柱形图','饼图']
        self.ComboTypeVar = StringVar(value='柱形图')
        self.ComboType = Combobox(self.FrameMain, state='readonly', text='柱形图', textvariable=self.ComboTypeVar, values=self.ComboTypeList, font=('微软雅黑',10))
        self.ComboType.setText = lambda x: self.ComboTypeVar.set(x)
        self.ComboType.text = lambda : self.ComboTypeVar.get()
        self.ComboType.place(relx=0.196, rely=0.173, relwidth=0.267)

        self.LblFilterVar = StringVar(value='筛选:')
        self.style.configure('TLblFilter.TLabel', anchor='w', background='#FFE0C0', font=('微软雅黑',10))
        self.LblFilter = Label(self.FrameMain, text='筛选:', textvariable=self.LblFilterVar, style='TLblFilter.TLabel')
        self.LblFilter.setText = lambda x: self.LblFilterVar.set(x)
        self.LblFilter.text = lambda : self.LblFilterVar.get()
        self.LblFilter.place(relx=0.558, rely=0.193, relwidth=0.090, relheight=0.175)

        self.LblViewVar = StringVar(value='视图类型:')
        self.style.configure('TLblView.TLabel', anchor='w', background='#FFE0C0', font=('微软雅黑',10))
        self.LblView = Label(self.FrameMain, text='视图类型:', textvariable=self.LblViewVar, style='TLblView.TLabel')
        self.LblView.setText = lambda x: self.LblViewVar.set(x)
        self.LblView.text = lambda : self.LblViewVar.get()
        self.LblView.place(relx=0.04, rely=0.607, relwidth=0.150, relheight=0.175)

        self.LblTypeVar = StringVar(value='图表类型:')
        self.style.configure('TLblType.TLabel', anchor='w', background='#FFE0C0', font=('微软雅黑',10))
        self.LblType = Label(self.FrameMain, text='图表类型:', textvariable=self.LblTypeVar, style='TLblType.TLabel')
        self.LblType.setText = lambda x: self.LblTypeVar.set(x)
        self.LblType.text = lambda : self.LblTypeVar.get()
        self.LblType.place(relx=0.04, rely=0.193, relwidth=0.150, relheight=0.175)


class ChartOption_callback(ChartOption_ui):
    #这个类实现具体的事件处理回调函数。界面生成代码在ChartOption_ui中。
    def __init__(self, master=None):
        ChartOption_ui.__init__(self, master)

    def CmdSubmit_Cmd(self, event=None):
        #根据本地数据生成html

        print(self.ComboType.text())
        print(self.ComboView.text())
        print(self.ComboFilter.text())

    def EV_WM_DELETE_WINDOW(self, event=None):
        #窗口退出消息
        self.master.destroy()

def ShowChart():
    top = Tk()
    top.attributes("-topmost", True)
    top.iconbitmap("Images/Icon.ico")
    ChartOption_callback(top).mainloop()

