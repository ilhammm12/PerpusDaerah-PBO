from PyQt5 import QtGui, QtWidgets
from PyQt5.QtWidgets import QPushButton


class QPushButtonComponent(QPushButton):

    def __init__(self, text):
        super().__init__()
        self.setStyleSheet("background-color : rgb(178,34,34);\n"
                           "border : none;\n"
                           "border-radius : 2px;\n"
                           "height : 30%;\n"
                           "color : white;")
        self.setText(text)
        font = QtGui.QFont()
        font.setFamily("Sans Serif")
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(65)

        self.setFont(font)

        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.sizePolicy().hasHeightForWidth())

        self.setSizePolicy(sizePolicy)