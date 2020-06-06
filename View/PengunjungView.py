import sys

from PyQt5.QtWidgets import *
from PyQt5.QtCore import QDate
from View.Component.QPushButtonComponent import QPushButtonComponent
from Class.Pengunjung import Pengunjung
from Model.Orm.OrmPengunjung import OrmPengunjung

class PengunjungView(QDialog):

    def __init__(self):
        super(PengunjungView, self).__init__()
        self.setWindowTitle("Form Pengunjung")
        self.resize(750, 350)
        self.UI()
        self.disableform()

    def UI(self):
        self.buatform()
        self.buattabelpengunjung()

        self.layoutUtama = QVBoxLayout()
        self.layouttabel = QHBoxLayout()
        self.layoutCrud = QHBoxLayout()

        self.btntambah = QPushButtonComponent("Berkunjung")
        self.btntambah.clicked.connect(self.enableform)
        
        self.layoutCrud.addWidget(self.btntambah)
        self.layouttabel.addWidget(self.tablepengunjung)
        self.btntambah.clicked.connect(self.enableform)
        self.formpengunjung.addRow(self.layouttabel)
        self.formpengunjung.addRow(self.layoutCrud)

        self.layoutUtama.addLayout(self.layoutCrud)
        self.setLayout(self.layoutUtama)

    def buatform(self):
        # formlayout
        self.formpengunjung = QFormLayout(self)
        # data inputan

        self.nama = QLineEdit(self)
        self.nama.setPlaceholderText("Nama")
        self.formpengunjung.addRow("Nama      ", self.nama)

        self.alamat = QTextEdit(self)
        self.alamat.setPlaceholderText("Alamat")
        self.alamat.setFixedHeight(50)
        self.formpengunjung.addRow("Alamat        ", self.alamat)

        self.nohp = QLineEdit(self)
        self.nohp.setInputMask("+62 9999 9999 999")
        self.formpengunjung.addRow("No Handphone      ", self.nohp)

        self.tglberkunjung = QDateEdit(self)
        self.tglberkunjung.setDisplayFormat('dd/MM/yyyy')
        self.tglberkunjung.setDate(QDate.currentDate())
        self.tglberkunjung.setReadOnly(True)
        self.formpengunjung.addRow("Tanggal Berkunjung        ", self.tglberkunjung)

        # button
        self.btn_simpan = QPushButtonComponent("SIMPAN")
        self.btn_simpan.setFixedHeight(45)
        self.btn_simpan.clicked.connect(self.submit_btn)
        self.formpengunjung.addRow(self.btn_simpan)

    def buattabelpengunjung(self):
        self.buattabel()

    def buattabel(self):
        self.tablepengunjung = QTableWidget()
        self.tablepengunjung.cellClicked.connect(self.cek)
        self.tablepengunjung.setColumnCount(5)
        self.tablepengunjung.setHorizontalHeaderLabels(
            ["Id Pengunjung","Nama","Alamat","NoHandphone","Tanggal Berkunjung"])
        self.tablepengunjung.setFixedSize(900, 350)
        self.tablepengunjung.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.isiTable()

    def cek(self, row):
        print(self.tablepengunjung.item(row, 0).text())
        print(self.tablepengunjung.item(row, 1).text())
        print(self.tablepengunjung.item(row, 2).text())
        print(self.tablepengunjung.item(row, 3).text())
        print(self.tablepengunjung.item(row, 4).text())

    def isiTable(self):
        query = OrmPengunjung.tampilpengunjung()
        self.tablepengunjung.setRowCount(len(query))
        for row in range(len(query)):
            self.tablepengunjung.setItem(row, 0, QTableWidgetItem(str(query[row].IdPengunjung)))
            self.tablepengunjung.setItem(row, 1, QTableWidgetItem(str(query[row].Nama)))
            self.tablepengunjung.setItem(row, 2, QTableWidgetItem(str(query[row].Alamat)))
            self.tablepengunjung.setItem(row, 3, QTableWidgetItem(query[row].NoHp))
            self.tablepengunjung.setItem(row, 4, QTableWidgetItem(query[row].TanggalBerkunjung))

    def submit_btn(self):
        try:
            Pengunjung(self.nama.text(),
                       self.alamat.toPlainText(),
                       self.nohp.text(),
                       self.tglberkunjung.text())

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
        self.nama.setReadOnly(True)
        self.alamat.setReadOnly(True)
        self.nohp.setReadOnly(True)
        self.btn_simpan.setDisabled(True)

    def enableform(self):
        self.nama.setReadOnly(False)
        self.alamat.setReadOnly(False)
        self.nohp.setReadOnly(False)
        self.btn_simpan.setDisabled(False)
        self.nama.setFocus()

    def refresh(self):
        self.nama.clear()
        self.alamat.clear()
        self.nohp.clear()

def tes():
    app = QApplication(sys.argv)
    win = PengunjungView()
    win.show()
    sys.exit(app.exec_())

tes()