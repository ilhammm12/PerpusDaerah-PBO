import sys

from PyQt5.QtWidgets import *
from Model.Orm.OrmAnggota import OrmAnggota
from View.Component.QPushButtonComponent import QPushButtonComponent
from Class.User import User
from Model.Orm.OrmUser import OrmUser


class UserView(QWidget):

    def __init__(self):
        super(UserView,self).__init__()
        self.setWindowTitle("Data User")
        self.resize(750, 350)
        self.UI()
        self.disableform()


    def UI(self):
        self.buatform()
        self.buattabeluser()
        self.layoutUtama = QVBoxLayout()
        self.layouttabel = QHBoxLayout()
        self.layoutCrud = QHBoxLayout()

        self.btntambah = QPushButtonComponent("Tambah")
        self.btnedit = QPushButtonComponent("Edit")
        self.btnhapus = QPushButtonComponent("Hapus")

        self.layoutCrud.addWidget(self.btntambah)
        self.layoutCrud.addWidget(self.btnedit)
        self.layoutCrud.addWidget(self.btnhapus)
        self.layouttabel.addWidget(self.tableuser)

        self.btntambah.clicked.connect(self.enableform)
        # self.btnedit.clicked.connect(lambda: self.editanggota())
        # self.btnhapus.clicked.connect(self.hapusAnggotaId)
        self.formuser.addRow(self.layouttabel)
        self.formuser.addRow(self.layoutCrud)

        # self.layoutUtama.addLayout(self.layouttabel)
        self.layoutUtama.addLayout(self.layoutCrud)
        self.setLayout(self.layoutUtama)


    def buatform(self):
        # formlayout
        self.formuser = QFormLayout(self)

        # data inputab
        self.username = QLineEdit(self)
        self.username.setPlaceholderText("Username")
        self.formuser.addRow("Usename        ", self.username)

        self.passwrd = QLineEdit(self)
        self.passwrd.setPlaceholderText("Password")
        self.formuser.addRow("Password       ", self.passwrd)

        self.hakakses = QComboBox()
        self.hakakses.addItem("Admin")
        self.hakakses.addItem("Petugas")
        self.formuser.addRow("Hak Akses      ", self.hakakses)
        # button
        self.btn_simpan = QPushButtonComponent("SIMPAN")
        self.btn_simpan.setFixedHeight(45)
        self.btn_simpan.clicked.connect(self.simpan_btn)
        self.formuser.addRow(self.btn_simpan)


    def buattabeluser(self):
        self.buattabel()

    def buattabel(self):
        self.tableuser = QTableWidget(self)
        self.tableuser.setColumnCount(4)
        self.tableuser.setHorizontalHeaderLabels(
            ["IdUser", "Username", "Password", "Hak Akses"])
        self.tableuser.setFixedSize(900, 350)
        self.tableuser.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.isiTable()

    def isiTable(self):
        query = OrmUser.tampiluser()

        self.tableuser.setRowCount(len(query))
        for row in range(len(query)):
            self.tableuser.setItem(row, 0, QTableWidgetItem(str(query[row].id_username)))
            self.tableuser.setItem(row, 1, QTableWidgetItem(str(query[row].username)))
            self.tableuser.setItem(row, 2, QTableWidgetItem(str(query[row].password)))
            self.tableuser.setItem(row, 3, QTableWidgetItem(str(query[row].hak_akses)))

    def simpan_btn(self):
        try:

            User(self.username.text(),
                    self.passwrd.text(),
                    self.hakakses.currentText())

            msg = QMessageBox()
            msg.setIcon(QMessageBox.Information)
            msg.setText("Data Telah Disimpan")
            msg.setWindowTitle("Berhasil")
            msg.exec_()
            self.refresh()
            self.disableform()
            self.isiTable()
        except Exception as e:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Information)

            msg.setText("Data tidak berhasil disimpan")
            msg.setInformativeText(f"ERROR : {e}")
            msg.setWindowTitle("Warning")
            msg.exec_()



    def disableform(self):

        self.username.setReadOnly(True)
        self.passwrd.setReadOnly(True)
        self.hakakses.setDisabled(True)
        self.btn_simpan.setDisabled(True)

    def enableform(self):
        self.username.setReadOnly(False)
        self.passwrd.setReadOnly(False)
        self.hakakses.setDisabled(False)
        self.btn_simpan.setDisabled(False)
        self.username.setFocus()

    def refresh(self):
        self.username.clear()
        self.passwrd.clear()



def tes():
    app = QApplication(sys.argv)
    win = UserView()
    win.show()
    sys.exit(app.exec_())
