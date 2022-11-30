import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QImage, QPixmap
from PyQt5.QtWidgets import QMessageBox
from subprocess import call
import requests


class Ui_Blacklist(object):
    def setupUi(self, Blacklist, List):
        Blacklist.setObjectName("Blacklist")
        Blacklist.resize(532, 331)
        self.Scroll_Area = QtWidgets.QScrollArea(Blacklist)
        self.Scroll_Area.setGeometry(QtCore.QRect(0, 0, 531, 331))
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.Scroll_Area.sizePolicy().hasHeightForWidth())
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
                                       "    border: 1px solid black;\n"
                                       "    background-color: rgb(240,248,255);\n"
                                       "}")
        self.Scroll_Area.setHorizontalScrollBarPolicy(
            QtCore.Qt.ScrollBarAsNeeded)
        self.Scroll_Area.setWidgetResizable(True)
        self.Scroll_Area.setAlignment(
            QtCore.Qt.AlignBottom | QtCore.Qt.AlignJustify)
        self.Scroll_Area.setObjectName("Scroll_Area")
        self.scrollAreaWidgetContents_2 = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_2.setGeometry(
            QtCore.QRect(0, 0, 529, 329))
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
        self.scrollAreaWidgetContents_2.setObjectName(
            "scrollAreaWidgetContents_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(
            self.scrollAreaWidgetContents_2)
        self.verticalLayout_2.setObjectName("verticalLayout_2")

        self.addList = []
        self.name = []
        self.OnOffList = []
        for i in range(len(List)):
            arr = List[i]
            self.Outer_frame = QtWidgets.QFrame(
                self.scrollAreaWidgetContents_2)
            sizePolicy = QtWidgets.QSizePolicy(
                QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
            sizePolicy.setHorizontalStretch(0)
            sizePolicy.setVerticalStretch(0)
            sizePolicy.setHeightForWidth(
                self.Outer_frame.sizePolicy().hasHeightForWidth())
            self.Outer_frame.setSizePolicy(sizePolicy)
            self.Outer_frame.setMinimumSize(QtCore.QSize(343, 100))
            palette = QtGui.QPalette()
            self.Outer_frame.setPalette(palette)
            self.Outer_frame.setAutoFillBackground(True)
            self.Outer_frame.setStyleSheet("background-color: rgb(#aaaaff);\n"
                                           "")
            self.Outer_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
            self.Outer_frame.setFrameShadow(QtWidgets.QFrame.Raised)
            self.Outer_frame.setObjectName("Outer_frame" + str(arr[0]))

            # Background
            self.Layer = QtWidgets.QLabel(self.Outer_frame)
            self.Layer.setEnabled(True)
            self.Layer.setGeometry(QtCore.QRect(0, 0, 511, 100))
            self.Layer.setMinimumSize(QtCore.QSize(0, 100))
            palette = QtGui.QPalette()
            brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
            brush.setStyle(QtCore.Qt.SolidPattern)
            palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
            brush = QtGui.QBrush(QtGui.QColor(170, 170, 255))
            brush.setStyle(QtCore.Qt.SolidPattern)
            palette.setBrush(QtGui.QPalette.Active,
                             QtGui.QPalette.Window, brush)
            brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
            brush.setStyle(QtCore.Qt.SolidPattern)
            palette.setBrush(QtGui.QPalette.Inactive,
                             QtGui.QPalette.Base, brush)
            brush = QtGui.QBrush(QtGui.QColor(170, 170, 255))
            brush.setStyle(QtCore.Qt.SolidPattern)
            palette.setBrush(QtGui.QPalette.Inactive,
                             QtGui.QPalette.Window, brush)
            brush = QtGui.QBrush(QtGui.QColor(170, 170, 255))
            brush.setStyle(QtCore.Qt.SolidPattern)
            palette.setBrush(QtGui.QPalette.Disabled,
                             QtGui.QPalette.Base, brush)
            brush = QtGui.QBrush(QtGui.QColor(170, 170, 255))
            brush.setStyle(QtCore.Qt.SolidPattern)
            palette.setBrush(QtGui.QPalette.Disabled,
                             QtGui.QPalette.Window, brush)
            self.Layer.setPalette(palette)
            self.Layer.setAutoFillBackground(True)
            self.Layer.setStyleSheet("#Layer{\n"
                                     "    background-color: rgb(#aaaaff);\n"
                                     "}")
            self.Layer.setText("")
            self.Layer.setObjectName("Layer" + str(arr[0]))

            # Button frame
            self.Button_frame = QtWidgets.QFrame(self.Outer_frame)
            self.Button_frame.setGeometry(QtCore.QRect(330, 30, 141, 51))
            self.Button_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
            self.Button_frame.setFrameShadow(QtWidgets.QFrame.Raised)
            self.Button_frame.setObjectName("Button_frame" + str(arr[0]))
            self.horizontalLayout_31 = QtWidgets.QHBoxLayout(self.Button_frame)
            self.horizontalLayout_31.setObjectName(
                "horizontalLayout_31" + str(arr[0]))

            self.Ban = QtWidgets.QPushButton(self.Button_frame)
            self.Ban.setObjectName(str(arr[0]))
            self.horizontalLayout_31.addWidget(self.Ban)

            # Information
            self.Info = QtWidgets.QFrame(self.Outer_frame)
            self.Info.setGeometry(QtCore.QRect(10, 10, 200, 81))
            self.Info.setMinimumSize(QtCore.QSize(200, 0))
            self.Info.setStyleSheet("#Info{\n"
                                    "    opacity: 0;\n"
                                    "}")
            self.Info.setFrameShape(QtWidgets.QFrame.StyledPanel)
            self.Info.setFrameShadow(QtWidgets.QFrame.Raised)
            self.Info.setObjectName("Info" + str(arr[0]))

            self.horizontalLayout_32 = QtWidgets.QHBoxLayout(self.Info)
            self.horizontalLayout_32.setSpacing(5)
            self.horizontalLayout_32.setObjectName(
                "horizontalLayout_32" + str(arr[0]))

            # Avatar
            self.ImageReal = QtWidgets.QLabel(self.Info)
            self.ImageReal.setMinimumSize(QtCore.QSize(50, 40))
            self.ImageReal.setText("")
            if (arr[3] != ''):
                image = QImage()
                image.loadFromData(requests.get(arr[3]).content)
                self.ImageReal.setPixmap(QPixmap(image))
                self.ImageReal.setScaledContents(True)
            else:
                self.ImageReal.setStyleSheet(
                    "border-image: url(./image/addfriend.png)"
                )
            self.ImageReal.setObjectName("ImageReal" + str(arr[0]))
            self.ImageReal.raise_()
            self.horizontalLayout_32.addWidget(self.ImageReal)

            # Info Box
            self.InfoBox = QtWidgets.QFrame(self.Info)
            sizePolicy = QtWidgets.QSizePolicy(
                QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
            sizePolicy.setHorizontalStretch(0)
            sizePolicy.setVerticalStretch(0)
            sizePolicy.setHeightForWidth(
                self.InfoBox.sizePolicy().hasHeightForWidth())
            self.InfoBox.setSizePolicy(sizePolicy)
            self.InfoBox.setMinimumSize(QtCore.QSize(100, 40))
            self.InfoBox.setFrameShape(QtWidgets.QFrame.StyledPanel)
            self.InfoBox.setFrameShadow(QtWidgets.QFrame.Raised)
            self.InfoBox.setObjectName("InfoBox" + str(arr[0]))

            ## Name and Status
            self.verticalLayout_12 = QtWidgets.QVBoxLayout(self.InfoBox)
            self.verticalLayout_12.setContentsMargins(-1, 2, -1, 2)
            self.verticalLayout_12.setObjectName(
                "verticalLayout_12" + str(arr[0]))
            Name = QtWidgets.QLabel(self.InfoBox)
            Name.setObjectName("Name" + str(arr[0]))
            self.verticalLayout_12.addWidget(Name)

            self.Status = QtWidgets.QFrame(self.InfoBox)
            self.Status.setFrameShape(QtWidgets.QFrame.StyledPanel)
            self.Status.setFrameShadow(QtWidgets.QFrame.Raised)
            self.Status.setObjectName("Status" + str(arr[0]))

            self.horizontalLayout_33 = QtWidgets.QHBoxLayout(self.Status)
            self.horizontalLayout_33.setContentsMargins(9, 9, 9, -1)
            self.horizontalLayout_33.setSpacing(5)
            self.horizontalLayout_33.setObjectName(
                "horizontalLayout_33" + str(arr[0]))

            self.IMG = QtWidgets.QLabel(self.Status)
            self.IMG.setAlignment(QtCore.Qt.AlignCenter)
            self.IMG.setObjectName("IMG" + str(arr[0]))
            self.horizontalLayout_33.addWidget(self.IMG)

            self.OnOff = QtWidgets.QLabel(self.Status)
            self.OnOff.setObjectName("OnOff" + str(arr[0]))

            self.horizontalLayout_33.addWidget(self.OnOff)
            self.verticalLayout_12.addWidget(self.Status)
            self.horizontalLayout_32.addWidget(self.InfoBox)
            self.verticalLayout_2.addWidget(self.Outer_frame)
            self.addList.append(self.Ban)
            self.name.append(Name)
            self.OnOffList.append(self.OnOff)
            self.retranslateBt(arr)

        self.Scroll_Area.setWidget(self.scrollAreaWidgetContents_2)
        self.Scroll_Area.raise_()
        self.retranslateUi(Blacklist)
        QtCore.QMetaObject.connectSlotsByName(Blacklist)

    def retranslateBt(self, arr):
        _translate_ = QtCore.QCoreApplication.translate
        self.addList[arr[0]].setText(_translate_("Blacklist", "Ban"))
        if (arr[1] == ''):
            self.name[arr[0]].setText(_translate_(
                "Blacklist", "Chưa có user nào đăng ký"))
        else:
            self.name[arr[0]].setText(_translate_("Blacklist", arr[1]))

        self.OnOffList[arr[0]].setText(_translate_("Blacklist", "Online"))

    def retranslateUi(self, Blacklist):
        _translate = QtCore.QCoreApplication.translate
        Blacklist.setWindowTitle(_translate("Blacklist", "Blacklist"))
        self.Ban.setText(_translate("Blacklist", "Ban"))


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    Blacklist = QtWidgets.QDialog()
    ui = Ui_Blacklist()
    ui.setupUi(Blacklist)
    Blacklist.show()
    sys.exit(app.exec_())