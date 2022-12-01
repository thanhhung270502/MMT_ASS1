import threading
import socket
import time
from PyQt5.QtCore import QThread, QObject, pyqtSignal as Signal, pyqtSlot as Slot
import os
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


    fileOK=Signal(bool)
    dataDone=Signal(bool)
    
    def catchMsg(self):
        sentence=self.connection.recv(1024).decode()
        print(f"From catchMsg:{sentence}")
        #time.sleep(12000)
        if(sentence=="#QUIT#"): 
            self.connection.send("#QUIT#".encode())
            time.sleep(1)
            self.connection.close()
            self.shutdown.emit(True)
        elif(sentence[:9]=="#CONTENT#"): self.catchMessage.emit((sentence[9:],0))
        elif(sentence[:6]=="#FILE#"):
            info=sentence[6:].split("#")
            name=info[0]
            size=info[1]
            print(f"Name: {name}, size:{size}")
            self.connection.send("#FILEOK#".encode())
            self.writeFile(name,size)
        elif(sentence=="#FILEOK#"):
            print("File OK")
            self.fileOK.emit(True)
        elif(sentence=="#COMPLETED#"):
            print("File Done")
            self.dataDone.emit(True)

    dataReceived=Signal(str)
    def writeFile(self,name,size):
        buffersize=max((int(int(size)/(1024*1024))+1)*1024,1024)
        print("File Writing")
        file=open(".\\Download\\"+name,"wb+")
        file_bytes=b""
        done=False
        while not done:
            data=self.connection.recv(buffersize)
            #print(f"From writeFile:{data.decode()}")
            file_bytes+=data
            if file_bytes[-5:]==b"#END#":
                done=True
            print(len(file_bytes))
        file.write(file_bytes[:-5])
        file.close()
        print("Out Loop")
        self.dataReceived.emit(name)
        self.connection.send("#COMPLETED#".encode())
        

class DataLink(QObject):
    def __init__(self,receiver,path):
        super().__init__()
        self.connection=receiver
        self.path=path
        self.name=path.split("\\")[-1]
        self.size=os.path.getsize(self.path)
        
    
    def send(self):
        self.connection.send(f"#FILE#{self.name}#{self.size}".encode())

    def sendBody(self):
        file=open(self.path,"rb")
        data=file.read()
        self.connection.sendall(data)
        self.connection.send(b"#END#")
        file.close()
        