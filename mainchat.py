import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QVBoxLayout
from UI_windowchat import *
from UI_userpage import *
import socket
import threading
import pymysql

username="LMN"

class WidgetWrap(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()

    def closeEvent(self,event):
        listenner.stop()

class Peer():
    def __init__(self):
        con = pymysql.connect(host="localhost",user="root",password="bucsehcmut2002",database="p2pchat")
        cur = con.cursor()
        cur.execute("select id, name, ip, picture from user")
            
        rows = cur.fetchall()
        lists = [list(x) for x in rows]


        self.friends= lists
        # self.friends = new_arr
        self.createUI()
    
    def createUI(self):
        app = QtWidgets.QApplication(sys.argv)
        AppChat = WidgetWrap()
        ui = Ui_AppChat()
        ui.setupUi(AppChat,self.friends)
        AppChat.show()
        sys.exit(app.exec_())




class Listenner():
    def __init__(self):
        self.client=[]
        self.serverPort=12000
        self.serverSocket=socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        self.serverSocket.bind(('',self.serverPort))
        self.serverSocket.listen(5)
        listenThread=threading.Thread(target=self.startListenning,args=())
        listenThread.setDaemon=True
        listenThread.start()
    
    def startListenning(self):
        print("Start listenning!!")
        while 1:  
            connectionSocket, addr = self.serverSocket.accept()
            thread=threading.Thread(target=self.service, args=(connectionSocket,))
            thread.daemon=True
            self.client.append(connectionSocket)
            thread.start()

    def service(self,connectionSocket):
        while True:
            sentence=connectionSocket.recv(1024).decode()
            pass
    
    def stop(self):
        print("Stop hearing")
        for conn in self.client:
            #Hoặc là ra tín hiệu để close
            conn.close()
        self.serverSocket.close()


if __name__ == "__main__":
    listenner=Listenner()
    peer=Peer()
