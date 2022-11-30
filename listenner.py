import threading
import socket
import time
from PyQt5.QtCore import QThread, QObject, pyqtSignal as Signal, pyqtSlot as Slot
from connect import *


class Listenner(QObject):
    catchConnection=Signal(object)
    

    def __init__(self,conn):
        super().__init__()
        self.connection=conn
    
    def listenWrapper(self):
        self.listen()

    

    @Slot(object)
    def listen(self):
        print("Listenning")
        connectionSocket, addr = self.connection.accept()
        endConn=False
        if(addr[0]==socket.gethostbyname(socket.gethostname())):
            endConn=True
        self.catchConnection.emit((connectionSocket,addr,endConn))
    
    
    
    def printss(self):
        print("Hi")

class Catcher(QObject):
    shutdown=Signal(bool)
    catchMessage=Signal(object)
    
    def __init__(self,receiver):
        super().__init__()
        self.connection=receiver
    
    def catchMsgWrapper(self):
        self.catchMsg()

    @Slot(object)
    def catchMsg(self):
        print("received")
        sentence=self.connection.recv(1024).decode()
        #time.sleep(12000)
        if(sentence=="#QUIT#"): 
            self.connection.send("#QUIT#".encode())
            time.sleep(1)
            self.connection.close()
            self.shutdown.emit(True)
        else: self.catchMessage.emit((sentence,0))