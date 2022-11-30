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
            host="localhost", user="root", password="", database="mmt")
        cur = con.cursor()
        cur.execute("select id, name, ip, image from user")
        rows = cur.fetchall()
        lists = [list(x) for x in rows]
        self.friends= lists
        self.createUI()

    def createUI(self):
        app = QtWidgets.QApplication(sys.argv)
        Addfriend = WidgetWrap()
        ui = Ui_Addfriend()
        ui.setupUi(Addfriend, self.friends)
        Addfriend.show()
        sys.exit(app.exec_())


if __name__ == "__main__":
    peer = Peer()