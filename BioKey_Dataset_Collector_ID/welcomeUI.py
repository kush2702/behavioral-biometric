# Form implementation generated from reading ui file 'welcomeUi.ui'
#
# Created by: PyQt6 UI code generator 6.2.3
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.

from pynput import keyboard
import sys
from http.client import OK
from tkinter import Button
from tkinter.messagebox import CANCEL
from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6.QtWidgets import QMessageBox
from q1 import Ui_Q1
from keyboardFeatureExtraction import keyboardFeatureExtraction as kfe
from helperMethods import Helper
from database import DataBaseConnector
class Ui_Welcome(object):

    def __init__(self) -> None:
        self.kfi = kfe()
        self.listener = keyboard.Listener(on_press=self.kfi.on_press,on_release=self.kfi.on_release)
        self.db = DataBaseConnector()

    def setupUi(self, Welcome):
        Welcome.setObjectName("Welcome")
        Welcome.resize(614, 370)
        self.centralwidget = QtWidgets.QWidget(Welcome)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.centralwidget.sizePolicy().hasHeightForWidth())
        self.centralwidget.setSizePolicy(sizePolicy)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(20, 20, 571, 321))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setSizeConstraint(QtWidgets.QLayout.SizeConstraint.SetNoConstraint)
        self.verticalLayout.setContentsMargins(3, 3, 3, 3)
        self.verticalLayout.setSpacing(3)
        self.verticalLayout.setObjectName("verticalLayout")
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.label = QtWidgets.QLabel(self.verticalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(18)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        self.verticalLayout.addItem(spacerItem1)
        self.label_3 = QtWidgets.QLabel(self.verticalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.MinimumExpanding, QtWidgets.QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_3.sizePolicy().hasHeightForWidth())
        self.label_3.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_3.setFont(font)
        self.label_3.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.verticalLayout.addWidget(self.label_3)
        spacerItem2 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        self.verticalLayout.addItem(spacerItem2)
        self.emailField = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.emailField.sizePolicy().hasHeightForWidth())
        self.emailField.setSizePolicy(sizePolicy)
        self.emailField.setText("")
        self.emailField.setObjectName("emailField")
        self.verticalLayout.addWidget(self.emailField)
        spacerItem3 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        self.verticalLayout.addItem(spacerItem3)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setSizeConstraint(QtWidgets.QLayout.SizeConstraint.SetNoConstraint)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.quitButton = QtWidgets.QPushButton(self.verticalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.quitButton.sizePolicy().hasHeightForWidth())
        self.quitButton.setSizePolicy(sizePolicy)
        self.quitButton.setObjectName("quitButton")
        self.horizontalLayout.addWidget(self.quitButton)
        self.weclomNextButton = QtWidgets.QPushButton(self.verticalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.weclomNextButton.sizePolicy().hasHeightForWidth())
        self.weclomNextButton.setSizePolicy(sizePolicy)
        self.weclomNextButton.setObjectName("weclomNextButton")
        self.horizontalLayout.addWidget(self.weclomNextButton)
        self.verticalLayout.addLayout(self.horizontalLayout)
        spacerItem4 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        self.verticalLayout.addItem(spacerItem4)
        self.verticalLayout.setStretch(0, 2)
        self.verticalLayout.setStretch(1, 2)
        self.verticalLayout.setStretch(2, 2)
        self.verticalLayout.setStretch(3, 2)
        self.verticalLayout.setStretch(4, 2)
        self.verticalLayout.setStretch(5, 2)
        self.verticalLayout.setStretch(6, 2)
        self.verticalLayout.setStretch(7, 2)
        self.verticalLayout.setStretch(8, 2)
        Welcome.setCentralWidget(self.centralwidget)

        self.retranslateUi(Welcome)
        QtCore.QMetaObject.connectSlotsByName(Welcome)
        
        self.emailField.returnPressed.connect(self.popupWin)
        self.weclomNextButton.clicked.connect(self.popupWin)
        self.quitButton.clicked.connect(Welcome.close)

    def retranslateUi(self, Welcome):
        _translate = QtCore.QCoreApplication.translate
        Welcome.setWindowTitle(_translate("Welcome", "MainWindow"))
        self.label.setText(_translate("Welcome", "Welcome, please insert your ID"))
        self.label_3.setText(_translate("Welcome", "ID :"))
        self.quitButton.setText(_translate("Welcome", "Quit"))
        self.weclomNextButton.setText(_translate("Welcome", "Next"))

    def popupWin(self):
        msgBox = QMessageBox()
        msgBox.setText("Are you shure the ID is correct?")
        msgBox.setWindowTitle("Check Agian")
        msgBox.setStandardButtons(QMessageBox.StandardButton.Ok | QMessageBox.StandardButton.Cancel)
        
        returnValue = msgBox.exec()
        if returnValue == QMessageBox.StandardButton.Ok:
            if Helper.checkId(id=self.emailField.text()):
                if not self.db.checkForDuplicate(id=self.emailField.text()):
                    self.kfi.setEmail(email=self.emailField.text())
                    Welcome.close()
                    self.startQ()
                else:
                    Helper.popupWinError(msg="ID allready in use")
                    self.emailField.clear()
            else:
                Helper.popupWinError(msg="Not a valid ID")
                self.emailField.clear()
                


    def startQ(self):
        self.window = QtWidgets.QDialog()
        self.ui = Ui_Q1(listener=self.listener, keboardfetureextractor=self.kfi)
        self.ui.setupUi(self.window)
        self.window.show()
        self.listener.start()

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Welcome = QtWidgets.QMainWindow()
    ui = Ui_Welcome()
    ui.setupUi(Welcome)
    Welcome.show()
    sys.exit(app.exec())