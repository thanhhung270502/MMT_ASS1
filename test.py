import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QVBoxLayout
from addfriend import *
import pymysql
import numpy as np


class WidgetWrap(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()


class Peer():
    def __init__(self):
        con = pymysql.connect(
            host="localhost", user="root", password="htkieT0964643875", database="docterapp")
        cur = con.cursor()
        cur.execute("select id,name,ip,picture from user")
        rows = cur.fetchall()
        arr = np.array(rows)
        self.friends = []
        for i in range(len(arr)):
            arr1 = np.array(rows[i])
            new_arr = []
            for j in range(len(arr1)):
                if j == 0:
                    new_arr.append(int(arr1[j]))
                else:
                    new_arr.append(arr1[j])
            self.friends.append(new_arr)
        self.createUI()

    def createUI(self):
        app = QtWidgets.QApplication(sys.argv)
        AddFriend = WidgetWrap()
        ui = Ui_Addfriend()
        ui.setupUi(AddFriend, self.friends)
        AddFriend.show()
        sys.exit(app.exec_())


if __name__ == "__main__":
    peer = Peer()
