#import sys
#import urllib.parse
#import threading
#from PyQt5.QtCore import QUrl
#from PyQt5.QtWidgets import QApplication
#from PyQt5.QtWebEngineWidgets import QWebEnginePage, QWebEngineView

#def ShowChart():
#    app = QApplication(sys.argv)
#    browser = QWebEngineView()
#    browser.load(QUrl("https://www.starlwr.com/chart.php?data="+urllib.parse.quote("2,1,QQ,8,微信,3")))
#    browser.show()
#    app.exec_()

import sys
import urllib.parse
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtWebEngineWidgets import *

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setWindowTitle('加载外部网页的例子')
        self.setGeometry(5,30,1355,730)
        self.browser=QWebEngineView()
        #加载外部的web界面
        self.browser.load(QUrl("https://www.starlwr.com/chart.php?data="+urllib.parse.quote("2,1,QQ,8,微信,3")))
        self.setCentralWidget(self.browser)

    def closeEvent(self, event):
        
        reply = QMessageBox.question(self, 'Message',
            "Are you sure to quit?", QMessageBox.Yes | 
            QMessageBox.No, QMessageBox.No)
 
        if reply == QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()

def ShowChart():
    app=QApplication(sys.argv)
    win=MainWindow()
    win.show()
    app.exit(app.exec_())

#import matplotlib.pyplot as plt

#def ShowChart():
#    labels='frogs','hogs','dogs','logs'
#    sizes=15,20,45,10
#    colors='yellowgreen','gold','lightskyblue','lightcoral'
#    explode=0,0.1,0,0
#    plt.pie(sizes,explode=explode,labels=labels,colors=colors,autopct='%1.1f%%',shadow=True,startangle=50)
#    plt.axis('equal')
#    plt.show()

    #import numpy as np
    #x=np.linspace(0,20)  #linspace()函数指定横坐标范围
    #plt.plot(x,.5+x)
    #plt.plot(x,1+2*x,'--')
    #plt.show()