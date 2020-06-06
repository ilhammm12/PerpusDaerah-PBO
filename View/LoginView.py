import sys

from PyQt5 import QtGui
from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt
from PyQt5.QtCore import pyqtSlot

from Model.Orm.OrmUser import OrmUser
from View.MenuView import MainMenuView
from View.Component.QEditLineComponent import QEditLineComponent
from View.Component.QFrameComponent import QFrameComponent
from View.Component.QLabelComponent import QLabelComponent
from View.Component.QPushButtonComponent import QPushButtonComponent

class LoginView(QWidget):
    def __init__(self):
        super().__init__()
        self.setFixedSize(400, 250)
        self.setWindowTitle("PERPUSTAKAAN DAERAH")

        self.font = QtGui.QFont()
        self.font.setFamily("Product Sans")
        self.font.setPointSize(12)
        self.font.setWeight(55)
        self.layoutUtama = QGridLayout()
        layout = QFrameComponent("")

        lbl_user = QLabelComponent("Username","black")
        lbl_user.setFont(self.font)
        self.txtusername = QEditLineComponent("")
        lbl_pass = QLabelComponent("Password","black")
        lbl_pass.setFont(self.font)
        self.txtpassword = QEditLineComponent("")
        self.txtpassword.setEchoMode(QLineEdit.Password)
        self.btnLogin = QPushButtonComponent("Login")
        self.btnLogin.setFont(self.font)

        self.layoutUtama.addWidget(layout, 4, 0, 1, 5, Qt.AlignTop)
        self.layoutUtama.addWidget(lbl_user, 1, 1, 1, 3, Qt.AlignLeft)
        self.layoutUtama.addWidget(self.txtusername, 2, 1, 1, 3)
        self.layoutUtama.addWidget(lbl_pass, 3, 1, 1, 3, Qt.AlignLeft)
        self.layoutUtama.addWidget(self.txtpassword, 4, 1, 1, 3)
        self.layoutUtama.addWidget(self.btnLogin, 4,1,2,3)
        self.btnLogin.clicked.connect(lambda : self.switchMainMenu())

        self.setLayout(self.layoutUtama)
        self.show()

    @pyqtSlot()
    def buttonClick(self):
        username = self.txtusername.text()
        password = self.txtpassword.text()
        checkLogin = OrmUser.user_login(username, password)
        if (checkLogin == True):
            self.switchMainMenu()
        else:
            msg = QMessageBox()
            msg.resize(250, 250)
            msg.setIcon(QMessageBox.Warning)
            msg.setText("Username atau Password Anda Salah!")
            msg.setWindowTitle("ERROR!")
            msg.exec_()

    @pyqtSlot()
    def switchMainMenu(self):
        # username = self.txtusername.text()
        # hakakses = OrmUser.findHakAkses(username)
        self.mainMenu = MainMenuView()
        self.mainMenu.show()
        self.hide()

    def clear(self):
        self.txtusername.setText("")
        self.txtpassword.setText("")
        self.txtusername.setFocus()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    loginView = LoginView()
    sys.exit(app.exec_())