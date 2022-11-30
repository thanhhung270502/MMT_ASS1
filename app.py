import res
import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox, QApplication, QMainWindow, QPushButton
from subprocess import call

serverIP="0.0.0.0"

class Ui_LogIn(object):

    def setupUi(self, LogIn):
        LogIn.setObjectName("LogIn")
        LogIn.resize(850, 750)
        LogIn.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        LogIn.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        self.LogIn = LogIn
        self.widget = QtWidgets.QWidget(LogIn)
        self.widget.setGeometry(QtCore.QRect(40, 30, 771, 670))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.widget.setFont(font)
        self.widget.setStyleSheet("QPushButton#BtSignIn{\n"
                                  "    background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(0, 0, 0, 255), stop:1 rgba(255, 255, 255, 255));\n"
                                  "    color: rgba(255,255,255,210);\n"
                                  "    border-radius: 5px;\n"
                                  "}\n"
                                  "QPushButton#BtSignIn:hover{\n"
                                  "    background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(50, 0, 0, 255), stop:1 rgba(255, 255, 150, 255));\n"
                                  "}\n"
                                  "QPushButton#BtSignIn:pressed{\n"
                                  "    padding-left: 5px;\n"
                                  "    padding-top: 5px;\n"
                                  "    background-color: gba(150,123,111,215);\n"
                                  "\n"
                                  "}")
        self.widget.setObjectName("widget")
        self.label = QtWidgets.QLabel(self.widget)
        self.label.setGeometry(QtCore.QRect(0, 0, 361, 670))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setStyleSheet("border-image: url(:/image/image/welcome.jpg);\n"
                                 "border-top-left-radius: 100px;\n"
                                 "background-color: rgba(0,0,0,80);")
        self.label.setText("")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.widget)
        self.label_2.setGeometry(QtCore.QRect(350, 0, 421, 670))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("background-color: rgba(255,255,255,255);\n"
                                   "border-bottom-right-radius: 100px;\n"
                                   "")
        self.label_2.setText("")
        self.label_2.setObjectName("label_2")
        self.Title = QtWidgets.QLabel(self.widget)
        self.Title.setGeometry(QtCore.QRect(460, 80, 211, 61))
        font = QtGui.QFont()
        font.setPointSize(32)
        font.setBold(True)
        font.setWeight(75)
        self.Title.setFont(font)
        self.Title.setStyleSheet("background-color: rgba(255,255,255,255);\n"
                                 "color: rgba(0,0,0,200);")
        self.Title.setObjectName("Title")
        self.Username = QtWidgets.QLineEdit(self.widget)
        self.Username.setGeometry(QtCore.QRect(410, 210, 301, 41))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(False)
        font.setUnderline(False)
        font.setWeight(50)
        self.Username.setFont(font)
        self.Username.setAutoFillBackground(False)
        self.Username.setStyleSheet("background-color: rgba(0,0,0,0);\n"
                                    "border: none;\n"
                                    "border-bottom: 2px solid rgba(46,82,101,200);\n"
                                    "color: rgba(0,0,0,240);\n"
                                    "padding-bottom: 7px;\n"
                                    "")
        self.Username.setObjectName("Username")
        self.Password = QtWidgets.QLineEdit(self.widget)
        self.Password.setGeometry(QtCore.QRect(410, 300, 301, 41))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(False)
        font.setUnderline(False)
        font.setWeight(50)
        self.Password.setFont(font)
        self.Password.setAutoFillBackground(False)
        self.Password.setStyleSheet("background-color: rgba(0,0,0,0);\n"
                                    "border: none;\n"
                                    "border-bottom: 2px solid rgba(46,82,101,200);\n"
                                    "color: rgba(0,0,0,240);\n"
                                    "padding-bottom: 7px;\n"
                                    "")
        self.Password.setEchoMode(QtWidgets.QLineEdit.Password)
        self.Password.setObjectName("Password")
        self.BtSignIn = QtWidgets.QPushButton(self.widget)
        self.BtSignIn.setGeometry(QtCore.QRect(470, 400, 171, 41))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.BtSignIn.setFont(font)
        self.BtSignIn.setObjectName("BtSignIn")
        self.BtForgotPassword = QtWidgets.QPushButton(self.widget)
        self.BtForgotPassword.setGeometry(QtCore.QRect(370, 520, 381, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(50)
        self.BtForgotPassword.setFont(font)
        self.BtForgotPassword.setStyleSheet("border: none;")
        self.BtForgotPassword.setObjectName("BtForgotPassword")
        self.BtSignUp = QtWidgets.QPushButton(self.widget)
        self.BtSignUp.setGeometry(QtCore.QRect(490, 470, 121, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setUnderline(True)
        font.setWeight(50)
        self.BtSignUp.setFont(font)
        self.BtSignUp.setStyleSheet("border: none;")
        self.BtSignUp.setObjectName("BtSignUp")
        self.label_3 = QtWidgets.QLabel(self.widget)
        self.label_3.setGeometry(QtCore.QRect(0, 110, 351, 261))
        self.label_3.setStyleSheet("background-color: rgba(0,0,0,75);")
        self.label_3.setText("")
        self.label_3.setObjectName("label_3")
        self.Txtnameapp = QtWidgets.QLabel(self.widget)
        self.Txtnameapp.setGeometry(QtCore.QRect(10, 130, 341, 61))
        font = QtGui.QFont()
        font.setPointSize(24)
        font.setBold(True)
        font.setWeight(75)
        self.Txtnameapp.setFont(font)
        self.Txtnameapp.setStyleSheet("color: rgba(255,255,255,210);")
        self.Txtnameapp.setObjectName("Txtnameapp")
        self.Txthello1 = QtWidgets.QLabel(self.widget)
        self.Txthello1.setGeometry(QtCore.QRect(10, 240, 331, 51))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.Txthello1.setFont(font)
        self.Txthello1.setStyleSheet("color: rgba(255,255,255,170);")
        self.Txthello1.setObjectName("Txthello1")
        self.Txthello2 = QtWidgets.QLabel(self.widget)
        self.Txthello2.setGeometry(QtCore.QRect(10, 280, 331, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.Txthello2.setFont(font)
        self.Txthello2.setStyleSheet("color: rgba(255,255,255,170);")
        self.Txthello2.setObjectName("Txthello2")
        self.Txthello3 = QtWidgets.QLabel(self.widget)
        self.Txthello3.setGeometry(QtCore.QRect(10, 320, 331, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.Txthello3.setFont(font)
        self.Txthello3.setStyleSheet("color: rgba(255,255,255,170);")
        self.Txthello3.setObjectName("Txthello3")
        self.BtExit = QtWidgets.QPushButton(self.widget)
        self.BtExit.setGeometry(QtCore.QRect(740, 0, 31, 28))
        self.BtExit.setStyleSheet("border-image: url(:/image/image/exit.png);")
        self.BtExit.setText("")
        self.BtExit.setObjectName("BtExit")

        self.retranslateUi(LogIn)
        QtCore.QMetaObject.connectSlotsByName(LogIn)

    def retranslateUi(self, LogIn):
        _translate = QtCore.QCoreApplication.translate
        LogIn.setWindowTitle(_translate("LogIn", "Form"))
        self.Title.setText(_translate("LogIn", "LOG IN"))
        self.Username.setPlaceholderText(_translate("LogIn", "Username"))
        self.Password.setPlaceholderText(_translate("LogIn", "Password"))
        self.BtSignIn.setText(_translate("LogIn", "Sign In"))
        self.BtForgotPassword.setText(_translate(
            "LogIn", "Forgot your Usename or Password?"))
        self.BtSignUp.setText(_translate("LogIn", "Sign Up"))
        self.Txtnameapp.setText(_translate("LogIn", "CHATVUIVE"))
        self.Txthello1.setText(_translate("LogIn", "Hi, we are CHATVUIVE"))
        self.Txthello2.setText(_translate("LogIn", "Welcome to our app!"))
        self.Txthello3.setText(_translate(
            "LogIn", "Have a good day with your friend!"))
        self.BtExit.clicked.connect(self.exit)
        self.BtSignIn.clicked.connect(self.signin)

    def signin(self):
        if self.Username.text() == "admin" and self.Password.text() == "admin":
            self.LogIn.close()
            call(["python", "mainchat.py"])
        else:
            mess = QMessageBox()
            mess.setIcon(QMessageBox.Warning)
            mess.setText("Sai tài khoản hoặc mật khẩu")

            mess.exec_()

    def exit(self):
        self.LogIn.close()


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    LogIn = QtWidgets.QWidget()
    ui = Ui_LogIn()
    ui.setupUi(LogIn)
    LogIn.show()
    sys.exit(app.exec_())