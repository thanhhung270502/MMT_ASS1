import threading
import socket
import sys
from UI_windowchat import *
import sys

class WidgetWrap(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()

    def closeEvent(self,event):
        self.conn.close()


def connStart(conn,arr):
    print(conn)
    app = QtWidgets.QApplication(sys.argv)
    AppChat = WidgetWrap()
    ui = Ui_MainChat()
    ui.setupUi(AppChat,arr,conn)
    AppChat.show()
    sys.exit(app.exec_())

if __name__=="__main__":
    arr=sys.argv[1:5]
    serverIP=arr[2]
    serverPort=12000
    clientSocket=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        clientSocket.connect((serverIP,serverPort))
    except:
        msg=QMessageBox()
        msg.setWindowTitle("Can't connect to this User!")
        msg.setText(f"The IP address:{serverIP} is unresponsive.")
        msg.setIcon(QMessageBox.Warning)
        msg.exec_()
    connStart(clientSocket,arr)