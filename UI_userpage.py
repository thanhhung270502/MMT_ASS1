from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QImage,QPixmap
from PyQt5.QtWidgets import QMessageBox
from subprocess import call
import requests
from UI_windowchat import *
from connect import *



class Ui_AppChat(object):
    

    def setupUi(self, AppChat,friendList):
        AppChat.setObjectName("AppChat")
        AppChat.resize(500, 600)
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(240, 248, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(240, 248, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(240, 248, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(240, 248, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(240, 248, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(240, 248, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(240, 248, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(240, 248, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(240, 248, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        AppChat.setPalette(palette)
        AppChat.setLayoutDirection(QtCore.Qt.RightToLeft)
        AppChat.setAutoFillBackground(False)
        AppChat.setStyleSheet("background-color: rgb(240,248,255);")
        self.centralwidget = QtWidgets.QWidget(AppChat)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.centralwidget.setFont(font)
        self.centralwidget.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.centralwidget.setObjectName("centralwidget")
        self.SetPicture = QtWidgets.QLabel(self.centralwidget)
        self.SetPicture.setGeometry(QtCore.QRect(10, 0, 100, 100))
        font = QtGui.QFont()
        self.SetPicture.setFont(font)
        self.SetPicture.setStyleSheet("border-image: url(./image/setpicture.jpg);\n"
"color: white;")
        self.SetPicture.setObjectName("SetPicture")
        self.BtCheckOnline = QtWidgets.QRadioButton(self.centralwidget)
        self.BtCheckOnline.setGeometry(QtCore.QRect(120, 0, 141, 31))
        self.BtCheckOnline.setStyleSheet("checked: checked;\n"
"accent-color: green;")
        self.BtCheckOnline.setText("")
        self.BtCheckOnline.setObjectName("BtCheckOnline")
        self.Username = QtWidgets.QLabel(self.centralwidget)
        self.Username.setGeometry(QtCore.QRect(150, 0, 101, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.Username.setFont(font)
        self.Username.setObjectName("Username")
        self.Status = QtWidgets.QComboBox(self.centralwidget)
        self.Status.setGeometry(QtCore.QRect(120, 30, 91, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.Status.setFont(font)
        self.Status.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.Status.setStyleSheet("background-color: rgb(240,248,255);\n"
"border: none;\n"
"color: green;\n"
"")
        self.Status.setObjectName("Status")
        self.Status.addItem("")
        self.Status.addItem("")
        self.Status.addItem("")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(120, 60, 370, 31))
        self.lineEdit.setStyleSheet("background-color: rgba(240,240,240,255);\n"
"color: black;")
        self.lineEdit.setObjectName("lineEdit")
        self.BtAddFriend = QtWidgets.QPushButton(self.centralwidget)
        self.BtAddFriend.setGeometry(QtCore.QRect(20, 120, 30, 30))
        self.BtAddFriend.setStyleSheet("border-image: url(E:/ComputerNetworking/ComputerNetworking/image/addfriend.png);")
        self.BtAddFriend.setText("")
        self.BtAddFriend.clicked.connect(self.callist)
        self.BtAddFriend.setObjectName("BtAddFriend")
        self.Search = QtWidgets.QLineEdit(self.centralwidget)
        self.Search.setGeometry(QtCore.QRect(55, 120, 435, 30))
        self.Search.setStyleSheet("background-color: rgba(240,240,240,255);\n"
"color: black;")
        self.Search.setObjectName("Search")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(20, 790, 70, 30))
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setUnderline(True)
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet("color: blue;\n"
"border: none;")
        self.pushButton.setObjectName("pushButton")
        self.Scroll_Area = QtWidgets.QScrollArea(self.centralwidget)
        self.Scroll_Area.setGeometry(QtCore.QRect(20, 160, 471, 421))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Scroll_Area.sizePolicy().hasHeightForWidth())
        self.Scroll_Area.setSizePolicy(sizePolicy)
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(240, 248, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(240, 248, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(240, 248, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(240, 248, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(240, 248, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(240, 248, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(240, 248, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(240, 248, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(240, 248, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        self.Scroll_Area.setPalette(palette)
        self.Scroll_Area.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        self.Scroll_Area.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.Scroll_Area.setStyleSheet("#Scroll_Area{\n"
"    border: 1px solid black\n"
"}")
        self.Scroll_Area.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
        self.Scroll_Area.setWidgetResizable(True)
        self.Scroll_Area.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignJustify)
        self.Scroll_Area.setObjectName("Scroll_Area")
        self.scrollAreaWidgetContents_2 = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_2.setGeometry(QtCore.QRect(0, 0, 469, 619))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(240, 248, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(240, 248, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(240, 248, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(240, 248, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(240, 248, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(240, 248, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(240, 248, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(240, 248, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(240, 248, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        self.scrollAreaWidgetContents_2.setPalette(palette)
        self.scrollAreaWidgetContents_2.setObjectName("scrollAreaWidgetContents_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.scrollAreaWidgetContents_2)
        self.verticalLayout_2.setObjectName("verticalLayout_2")

        ################################################################################################
        #Adding Friend
        #self.outerFrameList=[]
        #self.layerList=[]
        #self.buttonFrameList=[]
        #self.hLayout28List=[]
        self.removeList=[]
        self.chatList=[]
        #self.InfoFrame=[]
        #self.hLayout29List=[]
        #self.ImageReal=[]
        #self.InfoBoxList=[]
        #self.vLayout=[]
        self.name=[]
        #self.status=[]
        #self.hLayout30List=[]
        #self.IMG_8List=[]
        self.OnOffList=[]
        for i in range(len(friendList)):
            arr=friendList[i]
            #Setting up the frame
            outerFrame=QtWidgets.QFrame(self.scrollAreaWidgetContents_2)
            sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
            sizePolicy.setHorizontalStretch(0)
            sizePolicy.setVerticalStretch(0)
            sizePolicy.setHeightForWidth(outerFrame.sizePolicy().hasHeightForWidth())
            outerFrame.setSizePolicy(sizePolicy)
            outerFrame.setMinimumSize(QtCore.QSize(343, 100))
            palette = QtGui.QPalette()
            outerFrame.setPalette(palette)
            outerFrame.setAutoFillBackground(True)
            outerFrame.setStyleSheet("background-color: rgb(#aaaaff);\n"
            "")
            outerFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
            outerFrame.setFrameShadow(QtWidgets.QFrame.Raised)
            outerFrame.setObjectName("Outer_frame" + str(arr[0]))
        
            #Setting up the background
            layer= QtWidgets.QLabel(outerFrame)
            layer.setEnabled(True)
            layer.setGeometry(QtCore.QRect(0, 0, 451, 100))
            layer.setMinimumSize(QtCore.QSize(0, 100))
            palette = QtGui.QPalette()
            brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
            brush.setStyle(QtCore.Qt.SolidPattern)
            palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
            brush = QtGui.QBrush(QtGui.QColor(170, 170, 255))
            brush.setStyle(QtCore.Qt.SolidPattern)
            palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
            brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
            brush.setStyle(QtCore.Qt.SolidPattern)
            palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
            brush = QtGui.QBrush(QtGui.QColor(170, 170, 255))
            brush.setStyle(QtCore.Qt.SolidPattern)
            palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
            brush = QtGui.QBrush(QtGui.QColor(170, 170, 255))
            brush.setStyle(QtCore.Qt.SolidPattern)
            palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
            brush = QtGui.QBrush(QtGui.QColor(170, 170, 255))
            brush.setStyle(QtCore.Qt.SolidPattern)
            palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
            layer.setPalette(palette)
            layer.setAutoFillBackground(True)
            layer.setStyleSheet("#Layer_2{\n"
            "    background-color: rgb(#aaaaff);\n"
            "}")
            layer.setText("")
            layer.setObjectName("Layer" + str(arr[0]))

            #Setting up Button frame
            button_frame = QtWidgets.QFrame(outerFrame)
            button_frame.setGeometry(QtCore.QRect(290, 30, 141, 43))
            button_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
            button_frame.setFrameShadow(QtWidgets.QFrame.Raised)
            button_frame.setObjectName("Button_frame" + str(arr[0]))

            horizontalLayout28 = QtWidgets.QHBoxLayout(button_frame)
            horizontalLayout28.setObjectName("horizontalLayout28"+str(arr[0]))

            Remove_8 = QtWidgets.QPushButton(button_frame)
            Remove_8.setObjectName("Remove"+str(arr[0]))
           # Remove_8.clicked.connect(self.button_clicked)
            horizontalLayout28.addWidget(Remove_8)

            Chat_8 = QtWidgets.QPushButton(button_frame)
            Chat_8.setObjectName(str(arr[0]))
            Chat_8.clicked.connect(lambda x,ip=arr:self.connect(ip))
            horizontalLayout28.addWidget(Chat_8)


            #Setting up the Information Tabs
            Info_8 = QtWidgets.QFrame(outerFrame)
            Info_8.setGeometry(QtCore.QRect(10, 10, 200, 81))
            Info_8.setMinimumSize(QtCore.QSize(200, 0))
            Info_8.setStyleSheet("#Info_2{\n"
            "    opacity: 0;\n"
            "}")
            Info_8.setFrameShape(QtWidgets.QFrame.StyledPanel)
            Info_8.setFrameShadow(QtWidgets.QFrame.Raised)
            Info_8.setObjectName("Info"+str(arr[0]))

            horizontalLayout29 = QtWidgets.QHBoxLayout(Info_8)
            horizontalLayout29.setSpacing(5)
            horizontalLayout29.setObjectName("horizontalLayout29"+str(arr[0]))
            
            ##Avatar
            ImageReal_8 = QtWidgets.QLabel(Info_8)
            ImageReal_8.setMinimumSize(QtCore.QSize(50, 50))
            ImageReal_8.setMaximumSize(QtCore.QSize(50, 50))
            ImageReal_8.setText("")
            if(arr[3]!=''):
                image=QImage()
                image.loadFromData(requests.get(arr[3]).content)
                ImageReal_8.setPixmap(QPixmap(image))
                ImageReal_8.setScaledContents(True)
            else:
                ImageReal_8.setStyleSheet("border-image: url(./image/addfriend.png)")
            ImageReal_8.setObjectName("ImageReal"+str(arr[0]))
            ImageReal_8.raise_()
            horizontalLayout29.addWidget(ImageReal_8)

            #Info Box
            InfoBox_8 = QtWidgets.QFrame(Info_8)
            sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
            sizePolicy.setHorizontalStretch(0)
            sizePolicy.setVerticalStretch(0)
            sizePolicy.setHeightForWidth(InfoBox_8.sizePolicy().hasHeightForWidth())
            InfoBox_8.setSizePolicy(sizePolicy)
            InfoBox_8.setMinimumSize(QtCore.QSize(100, 40))
            InfoBox_8.setFrameShape(QtWidgets.QFrame.StyledPanel)
            InfoBox_8.setFrameShadow(QtWidgets.QFrame.Raised)
            InfoBox_8.setObjectName("InfoBox"+str(arr[0]))

            ##Name and Status
            verticalLayout_11 = QtWidgets.QVBoxLayout(InfoBox_8)
            verticalLayout_11.setContentsMargins(-1, 2, -1, 2)
            verticalLayout_11.setObjectName("verticalLayout"+str(arr[0]))

            Name_8 = QtWidgets.QLabel(InfoBox_8)
            Name_8.setObjectName("Name"+str(arr[0]))
            verticalLayout_11.addWidget(Name_8)

            Status_9 = QtWidgets.QFrame(InfoBox_8)
            Status_9.setFrameShape(QtWidgets.QFrame.StyledPanel)
            Status_9.setFrameShadow(QtWidgets.QFrame.Raised)
            Status_9.setObjectName("Status"+str(arr[0]))

            horizontalLayout_30 = QtWidgets.QHBoxLayout(Status_9)
            horizontalLayout_30.setContentsMargins(9, 9, 9, -1)
            horizontalLayout_30.setSpacing(5)
            horizontalLayout_30.setObjectName("horizontalLayout_30"+str(arr[0]))

            IMG_8 = QtWidgets.QLabel(Status_9)
            IMG_8.setAlignment(QtCore.Qt.AlignCenter)
            IMG_8.setObjectName("IMG_8"+str(arr[0]))

            horizontalLayout_30.addWidget(IMG_8)

            OnOff_8 = QtWidgets.QLabel(Status_9)
            OnOff_8.setObjectName("OnOff_8"+str(arr[0]))

            horizontalLayout_30.addWidget(OnOff_8)
            verticalLayout_11.addWidget(Status_9)
            horizontalLayout29.addWidget(InfoBox_8)

            self.verticalLayout_2.addWidget(outerFrame)

            ##This is for the appending to retrieve later
            #self.outerFrameList.append(outerFrame)
            #self.layerList.append(layer)
            #self.buttonFrameList.append(button_frame)
            #self.hLayout28List.append(horizontalLayout28)
            self.removeList.append(Remove_8)
            self.chatList.append(Chat_8)
            #self.InfoFrame.append(Info_8)
            #self.hLayout29List.append(horizontalLayout29)
            #self.ImageReal.append(ImageReal_8)
            #self.InfoBoxList.append(InfoBox_8)
            #self.vLayout.append(verticalLayout_11)
            self.name.append(Name_8)
            #self.status.append(Status_9)
            #self.hLayout30List.append(horizontalLayout_30)
            #self.IMG_8List.append(IMG_8)
            self.OnOffList.append(OnOff_8)

            ##Updating the Friend List with information
            self.retranslateBt(arr)
        ##########################################################
        ##########################################################
        self.Scroll_Area.setWidget(self.scrollAreaWidgetContents_2)
        self.BtCheckOnline.raise_()
        self.SetPicture.raise_()
        self.Username.raise_()
        self.Status.raise_()
        self.lineEdit.raise_()
        self.BtAddFriend.raise_()
        self.Search.raise_()
        self.pushButton.raise_()
        self.Scroll_Area.raise_()
        AppChat.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(AppChat)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 500, 23))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(False)
        font.setUnderline(True)
        font.setWeight(50)
        self.menubar.setFont(font)
        self.menubar.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.menubar.setStyleSheet("background-color: rgb(240,248,255);\n"
"color: blue;")
        self.menubar.setObjectName("menubar")
        self.menuUser = QtWidgets.QMenu(self.menubar)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.menuUser.setFont(font)
        self.menuUser.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.menuUser.setObjectName("menuUser")
        self.menuHelp = QtWidgets.QMenu(self.menubar)
        self.menuHelp.setObjectName("menuHelp")
        AppChat.setMenuBar(self.menubar)
        self.actionLogin = QtWidgets.QAction(AppChat)
        self.actionLogin.setObjectName("actionLogin")
        self.actionInformation = QtWidgets.QAction(AppChat)
        self.actionInformation.setObjectName("actionInformation")
        self.menuUser.addAction(self.actionInformation)
        self.menuUser.addAction(self.actionLogin)
        self.menubar.addAction(self.menuUser.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())

        self.retranslateUi(AppChat)
        QtCore.QMetaObject.connectSlotsByName(AppChat)

    def retranslateBt(self,arr):
        _translate = QtCore.QCoreApplication.translate
        self.removeList[arr[0]].setText(_translate("AppChat", "Remove"))
        self.chatList[arr[0]].setText(_translate("AppChat", "Chat"))
        if(arr[1]==''):
            self.name[arr[0]].setText(_translate("AppChat", 'Hãy kiếm thêm bạn'))
        else:
            self.name[arr[0]].setText(_translate("AppChat", arr[1]))
        self.OnOffList[arr[0]].setText(_translate("AppChat", "Online"))


    def retranslateUi(self, AppChat):
        _translate = QtCore.QCoreApplication.translate
        AppChat.setWindowTitle(_translate("AppChat", "Appchat"))
        self.SetPicture.setText(_translate("AppChat", "   SET PICTURE"))
        self.Username.setText(_translate("AppChat", "ZAC"))
        self.Status.setItemText(0, _translate("AppChat", "Online"))
        self.Status.setItemText(1, _translate("AppChat", "Busy"))
        self.Status.setItemText(2, _translate("AppChat", "Offline"))
        self.lineEdit.setPlaceholderText(_translate("AppChat", "Type your description here!"))
        self.Search.setPlaceholderText(_translate("AppChat", "Search friend"))
        self.pushButton.setText(_translate("AppChat", "Contact us"))
        self.menuUser.setTitle(_translate("AppChat", "User"))
        self.menuHelp.setTitle(_translate("AppChat", "Help"))
        self.actionLogin.setText(_translate("AppChat", "Logout"))
        self.actionInformation.setText(_translate("AppChat", "Information"))
    
    def connect(self,arr):
        threadConn=threading.Thread(target=createConn,args=(arr,))
        threadConn.daemon=True
        threadConn.start()
    


    def returnapp(self):
        self.AppChat.close()
        call(["python", "app.py"])

    def callist(self):
        call(["python", "listfriend.py"])



def createConn(arr):
    call(["python","connect.py",str(arr[0]),str(arr[1]),str(arr[2]),str(arr[3])])