# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainwindow.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets, QtCore, Qt
from PyQt5.QtWidgets import QFileDialog, QMessageBox
from PyQt5.QtGui import QMovie
import baike
import music
import cloud
import shutil,os
import time
import threading
import qdarkstyle
# LineEdit 文本路径
# LineEdit_7 百度百科
# LineEdit_8 歌手热评
# LineEdit_2 图片路径
# LineEdit_4 过滤词

#class Ui_MainWindow(QtWidgets.QMainWindow):
#    def __init__(self):
#        super(Ui_MainWindow,self).__init__()
#        self.setupUi(self)
#        self.retranslateUi(self)

signal_ = 0
keyword_ = ''
path_ = ''

class Ui_MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(Ui_MainWindow,self).__init__()
        self.setupUi(self)
        self.retranslateUi(self)
        self.work=False
    
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setEnabled(True)
        MainWindow.resize(716, 596)

        #创建整个界面的控件
        self.widget = QtWidgets.QWidget(MainWindow)
        self.widget.setEnabled(True)
        self.widget.setMinimumSize(QtCore.QSize(1024, 800))

        self.widget.setObjectName("widget")

        #创建该控件的布局，垂直布局
        self.verticalLayout = QtWidgets.QVBoxLayout(self.widget)
        #设置内容上下左右边界距离
        self.verticalLayout.setContentsMargins(11, 11, 11, 11)
        self.verticalLayout.setSpacing(6)
        self.verticalLayout.setObjectName("verticalLayout")

        #创建一个框
        self.groupBox = QtWidgets.QGroupBox(self.widget)
        self.groupBox.setObjectName("groupBox")
        #该框为水平布局
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.groupBox)
        self.horizontalLayout.setContentsMargins(2,2, 2, 2)
        #self.groupBox.setMinimumSize(QtCore.QSize(400,400))
        self.horizontalLayout.setSpacing(6)
        self.horizontalLayout.setObjectName("horizontalLayout")

        #文本
        self.groupBox_4 = QtWidgets.QGroupBox(self.groupBox)
        self.groupBox_4.setTitle("")
        self.groupBox_4.setObjectName("groupBox_4")
        self.groupBox_4.setMaximumSize(QtCore.QSize(1024,1024))
        self.groupBox_4.setMinimumSize(QtCore.QSize(400,200))
        #在groupBox_4中创建一个单选按键
        self.radioButton = QtWidgets.QRadioButton(self.groupBox_4)
        self.radioButton.setObjectName("radioButton")
        #self.groupBox_4 = QtWidgets.QGroupBox(self.groupBox)
        self.groupBox_4.setTitle("")
        self.groupBox_4.setObjectName("groupBox_4")
        self.gridLayout = QtWidgets.QGridLayout(self.groupBox_4)
        self.gridLayout.setContentsMargins(11, 11,0, 0)
        self.gridLayout.setSpacing(1)
        self.gridLayout.setObjectName("gridLayout")
        self.gridLayout.addWidget(self.radioButton,0,0,1,1)

        #创建一个输入文本框
        self.lineEdit = QtWidgets.QLineEdit(self.groupBox_4)
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit.setEnabled(False)
        #添加该文本输入框，指定位置
        self.gridLayout.addWidget(self.lineEdit, 1, 0, 1, 2)
        #创建一个...按钮
        self.toolButton_2 = QtWidgets.QToolButton(self.groupBox_4)
        self.toolButton_2.setObjectName("toolButton_2")
        self.toolButton_2.setEnabled(False)
        self.gridLayout.addWidget(self.toolButton_2, 1, 2, 1, 1)
        #在垂直布局中添加gruop_4
        #self.verticalLayout_2.addWidget(self.groupBox_4)

        #其他来源对应框
        '''
        self.groupBox_9 = QtWidgets.QGroupBox(self.groupBox_8)
        self.groupBox_9.setMinimumSize(QtCore.QSize(100,100))
        self.groupBox_9.setMaximumSize(QtCore.QSize(16777215, 100))
        self.groupBox_9.setTitle("")
        self.groupBox_9.setObjectName("groupBox_9")
        self.gridLayout_7 = QtWidgets.QGridLayout(self.groupBox_9)
        self.gridLayout_7.setContentsMargins(2, 2, 2, 2)
        self.gridLayout_7.setHorizontalSpacing(1)
        self.gridLayout_7.setVerticalSpacing(1)
        self.gridLayout_7.setObjectName("gridLayout_7")
        '''
        #关键字label
        self.label_9 = QtWidgets.QLabel(self.groupBox_4)
        self.label_9.setObjectName("label_9")
        self.gridLayout.addWidget(self.label_9, 3, 0, 1, 1)
        self.lineEdit_7 = QtWidgets.QLineEdit(self.groupBox_4)
        self.lineEdit_7.setObjectName("lineEdit_7")
        self.lineEdit_7.setEnabled(False)
        self.gridLayout.addWidget(self.lineEdit_7, 3, 1, 1, 1)
        #百度百科按钮
        self.radioButton_8 = QtWidgets.QRadioButton(self.groupBox_4)
        self.radioButton_8.setObjectName("radioButton_8")
        self.gridLayout.addWidget(self.radioButton_8, 2, 0, 1, 2)
        #歌手框
        #self.groupBox_10 = QtWidgets.QGroupBox(self.groupBox_8)
        #sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Fixed)
        #.setHorizontalStretch(0)
        #sizePolicy.setVerticalStretch(0)
        #sizePolicy.setHeightForWidth(self.groupBox_4.sizePolicy().hasHeightForWidth())
        #self.groupBox_4.setSizePolicy(sizePolicy)
        '''
        self.groupBox_10.setMaximumSize(QtCore.QSize(16777215, 100))
        self.groupBox_10.setTitle("")
        self.groupBox_10.setObjectName("groupBox_10")
        self.gridLayout_8 = QtWidgets.QGridLayout(self.groupBox_10)
        self.gridLayout_8.setContentsMargins(11, 5, 11, 5)
        self.gridLayout_8.setHorizontalSpacing(6)
        self.gridLayout_8.setVerticalSpacing(5)
        self.gridLayout_8.setObjectName("gridLayout_8")
        '''
        self.label_10 = QtWidgets.QLabel(self.groupBox_4)
        self.label_10.setObjectName("label_10")
        self.gridLayout.addWidget(self.label_10, 5, 0, 1, 1)
        self.lineEdit_8 = QtWidgets.QLineEdit(self.groupBox_4)
        self.lineEdit_8.setObjectName("lineEdit_8")
        self.lineEdit_8.setEnabled(False)
        self.gridLayout.addWidget(self.lineEdit_8, 5, 1, 1, 4)
        self.radioButton_9 = QtWidgets.QRadioButton(self.groupBox_4)
        self.radioButton_9.setObjectName("radioButton_9")
        self.gridLayout.addWidget(self.radioButton_9, 4, 0, 1, 2)
        #self.verticalLayout_2.addWidget(self.groupBox_10)

        #网易
        '''
        self.groupBox_11 = QtWidgets.QGroupBox(self.groupBox_8)
        self.groupBox_11.setMaximumSize(QtCore.QSize(16777215, 100))
        self.groupBox_11.setTitle("")
        self.groupBox_11.setObjectName("groupBox_11")
        self.gridLayout_9 = QtWidgets.QGridLayout(self.groupBox_11)
        self.gridLayout_9.setContentsMargins(11, 11, 11, 11)
        self.gridLayout_9.setSpacing(6)
        self.gridLayout_9.setObjectName("gridLayout_9")
        '''
        # self.radioButton_10 = QtWidgets.QRadioButton(self.groupBox_4)
        # self.radioButton_10.setObjectName("radioButton_10")
        # self.gridLayout.addWidget(self.radioButton_10, 6, 0, 1, 2)
        #self.verticalLayout_2.addWidget(self.groupBox_4)
        '''
        self.verticalLayout_2.setStretch(2, 1)
        self.verticalLayout_2.setStretch(3, 3)
        self.verticalLayout_2.setStretch(4, 2)
        self.verticalLayout_2.setStretch(5, 1)
        '''
        self.horizontalLayout.addWidget(self.groupBox_4)

        #加载图片
        self.l1 = QtWidgets.QLabel(self.groupBox)
        png = QtGui.QPixmap("empty.png")
        self.movie = QMovie("loading.gif")
        #self.l1.setMinimumSize(QtCore.QSize(100,100))
        #self.l1.setMaximumSize(QtCore.QSize(100,100))
        self.movie.setScaledSize(QtCore.QSize(50,50))
        self.l1.setMovie(self.movie)
        self.movie.start()
        self.l1.setPixmap(png)
        self.l1.setScaledContents(True)
        self.l1.setMinimumSize(QtCore.QSize(500,400)) 
        self.l1.setMaximumSize(QtCore.QSize(600, 600))
        self.horizontalLayout.addWidget(self.l1)
        '''
        self.graphicsView = QtWidgets.QGraphicsView(self.groupBox)
        self.graphicsView.setObjectName("graphicsView")
        self.horizontalLayout.addWidget(self.graphicsView)
        '''
        self.verticalLayout.addWidget(self.groupBox)
   
   		#辅助选项
        self.groupBox_2 = QtWidgets.QGroupBox(self.widget)
        self.groupBox_2.setMinimumSize(QtCore.QSize(200, 200))
        self.groupBox_2.setObjectName("groupBox_2")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.groupBox_2)
        self.gridLayout_3.setContentsMargins(1, 1, 1, 1)
        self.gridLayout_3.setSpacing(1)
        self.gridLayout_3.setObjectName("gridLayout_3")
        #字体
        self.label_4=QtWidgets.QLabel(self.groupBox_2)
        self.label_4.setObjectName("label_4")
        self.gridLayout_3.addWidget(self.label_4,3,0,1,1)
        self.font = QtWidgets.QComboBox(self.groupBox_2)
        self.font.setEnabled(True)
        self.font.setObjectName("font")
        self.fonts={"宋体":"simsun","黑体":"simhei","隶书":"SIMLI","简约":"simkai"}
        for i,j in self.fonts.items():
            self.font.addItem(i)
        self.gridLayout_3.addWidget(self.font, 3, 1, 1, 1)

        #自定义轮廓
        self.toolButton = QtWidgets.QToolButton(self.groupBox_2)
        self.toolButton.setObjectName("toolButton")
        self.gridLayout_3.addWidget(self.toolButton, 0, 4, 1, 1)
        #字体大小label
        self.label_5 = QtWidgets.QLabel(self.groupBox_2)
        self.label_5.setObjectName("label_5")
        self.gridLayout_3.addWidget(self.label_5, 1, 0, 1, 1)
        #mask_degree
        self.slider = QtWidgets.QSlider(QtCore.Qt.Horizontal)
        # self.slider.setOrientation(QtCore.Qt.Horizontal)
        self.slider.setObjectName("horizontalSlider")
        self.slider.setMinimum(0)
        self.slider.setMaximum(100)
        self.slider.setSingleStep(1)
        self.slider.setValue(50)
        self.slider.setTickPosition(QtWidgets.QSlider.TicksBelow)
        self.slider.setTickInterval(10)
        self.gridLayout_3.addWidget(self.slider,4, 1, 1, 2)
        # self.comboBox_2 = QtWidgets.QComboBox(self.groupBox_2)
        # self.comboBox_2.setObjectName("comboBox_2")
        # self.comboBox_2.setEnabled(True)

        # l={1:"0",2:"0.25",3:"0.5",4:"1"}
        # for i,j in l.items():
        # 	self.comboBox_2.addItem(j,i)

        # self.gridLayout_3.addWidget(self.comboBox_2, 4, 1, 1, 2)
        #maskdegree label
        self.label_3 = QtWidgets.QLabel(self.groupBox_2)
        self.label_3.setObjectName("label_3")
        self.gridLayout_3.addWidget(self.label_3, 4, 0, 1, 1)
        #字体大小选择
        self.fontSize = QtWidgets.QComboBox(self.groupBox_2)
        self.fontSize.setEnabled(True)
        self.fontSize.setObjectName("fontSize")
        stepsize=["1","2","4"]
        for i  in stepsize :
        	self.fontSize.addItem(i)
        self.gridLayout_3.addWidget(self.fontSize, 1, 1, 1, 2)

       	#自定义轮廓
        self.lineEdit_2 = QtWidgets.QLineEdit(self.groupBox_2)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.gridLayout_3.addWidget(self.lineEdit_2, 0, 1, 1, 3)
        self.label_6 = QtWidgets.QLabel(self.groupBox_2)
        self.label_6.setObjectName("label_6")
        self.gridLayout_3.addWidget(self.label_6, 2, 0, 1, 1)
        self.label_7 = QtWidgets.QLabel(self.groupBox_2)
        self.label_7.setObjectName("label_7")
        pe = Qt.QPalette()  
        pe.setColor(Qt.QPalette.WindowText,QtCore.Qt.blue)   
        pe.setColor(Qt.QPalette.Window,QtCore.Qt.blue)  
        #pe.setColor(QPalette.Background,Qt.blue)  
        self.label_7.setPalette(pe)  
        self.gridLayout_3.addWidget(self.label_7, 2, 2, 1, 1)
        self.radioButton_4 = QtWidgets.QRadioButton(self.groupBox_2)
        self.radioButton_4.setObjectName("radioButton_4")
        self.gridLayout_3.addWidget(self.radioButton_4, 0, 0, 1, 1)
        self.lineEdit_4 = QtWidgets.QLineEdit(self.groupBox_2)
        '''
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEdit_4.sizePolicy().hasHeightForWidth())
		'''
        #self.lineEdit_4.setSizePolicy(sizePolicy)
        self.lineEdit_4.setMinimumSize(QtCore.QSize(200, 10))
        self.lineEdit_4.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.gridLayout_3.addWidget(self.lineEdit_4, 2, 1, 1, 1) 
        self.verticalLayout.addWidget(self.groupBox_2)
        

        self.groupBox_6 = QtWidgets.QGroupBox(self.widget)
        self.groupBox_6.setObjectName("groupBox_6")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.groupBox_6)
        self.horizontalLayout_3.setContentsMargins(11, 11, 11, 11)
        self.horizontalLayout_3.setSpacing(6)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem)
        self.pushButton_2 = QtWidgets.QPushButton(self.groupBox_6)
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(self.groupBox_6)
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_3.setEnabled(False)
        self.horizontalLayout_3.addWidget(self.pushButton_2)
        self.horizontalLayout_3.addWidget(self.pushButton_3)
        self.verticalLayout.addWidget(self.groupBox_6)
        self.verticalLayout.setStretch(0, 7)
        self.verticalLayout.setStretch(1, 2)
        self.groupBox_7=QtWidgets.QGroupBox(self.widget)
        self.groupBox_7.setObjectName("groupBox_7")
        self.horizontalLayout_7=QtWidgets.QHBoxLayout(self.groupBox_7)
        self.horizontalLayout_7.setContentsMargins(11, 11, 11, 11)
        self.horizontalLayout_7.setSpacing(6)
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        #self.horizontalLayout_7.addItem(spacerItem)
        self.label_8=QtWidgets.QLabel(self.groupBox_7)
        self.label_8.setObjectName("label_8")
        self.label_8.setFont(QtGui.QFont("Roman times",15))  
        self.horizontalLayout_7.addStretch()
        self.horizontalLayout_7.addWidget(self.label_8)
        self.horizontalLayout_7.addStretch()
        self.verticalLayout.addWidget(self.groupBox_7)
        MainWindow.setCentralWidget(self.widget)

        #菜单
        self.menuBar = QtWidgets.QMenuBar(MainWindow)
        self.menuBar.setGeometry(QtCore.QRect(10, 10, 716, 22))
        self.menuBar.setObjectName("menuBar")
        self.file = self.menuBar.addMenu("File")
        self.file.addAction("New")
        self.save = QtWidgets.QAction("Save",self)
        self.save.setShortcut("Ctrl+S")
        self.file.addAction(self.save)

        MainWindow.setMenuBar(self.menuBar)


        self.toolBar = QtWidgets.QToolBar(MainWindow)
        self.toolBar.setObjectName("toolBar")
        MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.toolBar)
        self.statusBar = QtWidgets.QStatusBar(MainWindow)
        self.statusBar.setObjectName("statusBar")
        MainWindow.setStatusBar(self.statusBar)

        self.lineEdit_8.setMinimumSize(QtCore.QSize(150,20))
        self.lineEdit_8.setMaximumSize(QtCore.QSize(150,20))

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.eventSetup()

        # painter = QtGui.QPainter(self)
        # painter.setBrush(QtGui.QColor(255,0,0,127))
        # painter.drawRect(self.rect())

    #确认键槽函数
    # def paintEvent(self, event):
    #     painter = QtGui.QPainter(self)
    #     painter.setBrush(QtGui.QColor(255,0,0,127))
    #     painter.drawRect(self.rect())


    def confirm(self):
        print("Hello")
        signal_1 = self.radioButton.isChecked()
        signal_2 = self.radioButton_8.isChecked()
        signal_3 = self.radioButton_9.isChecked()
        signal_p = self.radioButton_4.isChecked()
        path = ''
        keyword = ''
        signal = 0
        #无输入错误提示框
        
        if signal_1 == True:
            if(self.lineEdit.text()== ''):
                er1_reply = QMessageBox.warning(self," ", "1你别搞事情好不好？",QMessageBox.Yes|QMessageBox.No,QMessageBox.Yes)
                print(er1_reply)
                return
            else:
                path = self.lineEdit.text()
                signal = 1

                #百度百科
        elif signal_2 == True:
            if self.lineEdit_7.text() == '':
                er1_reply = QMessageBox.warning(self," ", "2你别搞事情好不好？",QMessageBox.Yes|QMessageBox.No,QMessageBox.Yes)
                print(er1_reply)
                return
            else:
                keyword = self.lineEdit_7.text()
                signal = 2
#歌手热评
        elif signal_3 == True:
            if(self.lineEdit_8.text()== ''):
                er1_reply = QMessageBox.warning(self," ", "3你别搞事情好不好？",QMessageBox.Yes|QMessageBox.No,QMessageBox.Yes)
                print(er1_reply)
                return
            else:
                keyword = self.lineEdit_8.text()
                signal = 3
        #辅助选项
        picture_path = ''
        if signal_p == True:
            picture_path = self.lineEdit_2.text()
        step = int(self.fontSize.currentText())
        # stopword = ["首歌"]
        stopword = self.lineEdit_4.text().split('-')
        font=self.fonts[self.font.currentText()]+".ttf"
        masker_degree = self.slider.value()/100.0
        self.g_(path, keyword, signal, picture_path, step, stopword, font, masker_degree)
        _translate = QtCore.QCoreApplication.translate
        self.label_8.setText(_translate("MainWindow","生成完毕"))
        #self.label_8.setText("生成完毕")

    def g_(self,path, keyword, signal, picture_path, step, stopword, font, masker_degree):
        global signal_
        global keyword_
        global path_

        self.l1.setMovie(self.movie)
        self.movie.start()
        print("等待中……")

        if picture_path == '':
                picture_path = 'data/local/img.jpg'

        if signal == 1:
            print(cloud.draw_wordcloud(path, "white", font, picture_path, stopword, masker_degree, fontstep = step))
            # png = QtGui.QPixmap("data/local/result.jpg")
            # self.l1.setPixmap(png)

        elif signal == 2:
            if signal_ != signal or keyword_ != keyword:
                baike.getBaikeText(keyword)
                baike.getgBaikePhoto(keyword)
            print("Finish!")
            print(cloud.draw_wordcloud("data/local/comment.txt","white",font,"data/local/img.jpg",stopword,masker_degree,fontstep = step))
            # png = QtGui.QPixmap("data/local/result.jpg")
            # self.l1.setPixmap(png)

        elif signal == 3:
            print(signal_,signal)
            if signal_ != signal or keyword_ != keyword:
                music.singer_craw(keyword)
                print("path is" + "picture_path")
            print(cloud.draw_wordcloud("data/local/comment.txt","white",font, picture_path,stopword,masker_degree,fontstep = step))
            print("Finish!")
            # png = QtGui.QPixmap("data/local/result.jpg")
            # self.l1.setPixmap(png)

        png = QtGui.QPixmap("data/local/result.jpg")
        print(png.width())
        print(png.height())
        #scaredPng = png.scaled(400, 500, aspectRatioMode = QtCore.Qt.KeepAspectRatio)
        # self.l1.setPixmap(scaredPng)
        # wait(10)
        self.l1.setScaledContents(True)
        self.l1.setPixmap(png)

        signal_ = signal
        keyword_ = keyword
        path_ = path
        self.pushButton_3.setEnabled(True)


    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "词云生成器"))
        self.groupBox.setTitle(_translate("MainWindow", ""))
        self.radioButton.setText(_translate("MainWindow", "文本路径"))
        self.toolButton_2.setText(_translate("MainWindow", "..."))
        self.label_9.setText(_translate("MainWindow", "关键字"))
        self.radioButton_8.setText(_translate("MainWindow", "百度百科"))
        self.label_10.setText(_translate("MainWindow", "关键字"))
       	self.radioButton_9.setText(_translate("MainWindow", "歌手热评"))
        # self.radioButton_10.setText(_translate("MainWindow", "网易云热评"))
        self.groupBox_2.setTitle(_translate("MainWindow", "辅助选项"))
        self.label_4.setText(_translate("MainWindow", "字体"))
        self.toolButton.setText(_translate("MainWindow", "..."))
        self.label_5.setText(_translate("MainWindow", "步长"))
        self.label_3.setText(_translate("MainWindow", "masker degree"))
        self.label_6.setText(_translate("MainWindow", "过滤词"))
        self.label_7.setText(_translate("MainWindow", "（以“-”区分词语，如“一个-伙伴”）"))
        self.radioButton_4.setText(_translate("MainWindow", "图片（不选则使用默认图片）"))
        self.groupBox_6.setTitle(_translate("MainWindow", ""))
        self.pushButton_2.setText(_translate("MainWindow", "确认"))
        self.toolBar.setWindowTitle(_translate("MainWindow", "toolBar"))
        self.pushButton_3.setText(_translate("MainWindow", "保存"))
        self.label_8.setText("")

    def select_txt_File(self):
    	sender = self.sender()
    	directory,filetype=QFileDialog.getOpenFileName(self,"","C:/","(*.txt)")
    	print(directory)
    	self.lineEdit.setText(directory)

    def select_picture_File(self):
    	directory,filetype=QFileDialog.getOpenFileName(self,"","C:/","(*.png)")
    	print(directory)
    	self.lineEdit_2.setText(directory)

    def Enable_local_txt(self):
    	self.lineEdit.setEnabled(True)
    	self.toolButton_2.setEnabled(True)
    	self.lineEdit_7.setEnabled(False)
    	self.lineEdit_8.setEnabled(False)

    def Enable_Baidu(self):
    	self.lineEdit.setEnabled(False)
    	self.toolButton_2.setEnabled(False)
    	self.lineEdit_7.setEnabled(True)
    	self.lineEdit_8.setEnabled(False)

    def Enable_Singer(self):
    	self.lineEdit.setEnabled(False)
    	self.toolButton_2.setEnabled(False)
    	self.lineEdit_7.setEnabled(False)
    	self.lineEdit_8.setEnabled(True)

    def Enable_WangYiyun(self):
    	self.lineEdit.setEnabled(False)
    	self.lineEdit_7.setEnabled(False)
    	self.lineEdit_8.setEnabled(False)
    	self.toolButton_2.setEnabled(False)

    def Save_picture(self):
        fileName2, ok2 = QFileDialog.getSaveFileName(self,  
                                    "文件保存",  
                                    "C:/",  
                                    "(*.jpg)")
        shutil.copy("./data/local/result.jpg",fileName2)


    def generate(self):
        g_cloud=threading.Thread(target=self.confirm,args=())
        _translate = QtCore.QCoreApplication.translate
        self.label_8.setText(_translate("MainWindow","词云正在生成"))
        g_cloud.start()

    def eventSetup(self):
        self.toolButton_2.clicked.connect(self.select_txt_File)
        self.toolButton.clicked.connect(self.select_picture_File)
        self.radioButton.clicked.connect(self.Enable_local_txt)
        self.radioButton_8.clicked.connect(self.Enable_Baidu)
        self.pushButton_3.clicked.connect(self.Save_picture)
        self.radioButton_9.clicked.connect(self.Enable_Singer)
    	# self.radioButton_10.clicked.connect(self.Enable_WangYiyun)
        self.pushButton_2.clicked.connect(self.generate)


import sys

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    new = Ui_MainWindow()
    # new.setStyleSheet(qdarkstyle.load_stylesheet_pyqt5())
    style = '''

        #MainWindow{
            border-image:url(timg.jpeg);
        }
    '''
    new.setStyleSheet(style)
    new.show()
    print("H")
    sys.exit(app.exec_())
    #os.system("pause")
