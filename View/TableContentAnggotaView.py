from PyQt5.QtWidgets import QGridLayout,QComboBox, QPushButton, QApplication, QAbstractItemView,QDialog, QMessageBox, QWidget, QHBoxLayout, QTableWidget, QTableWidgetItem, QVBoxLayout
import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt, pyqtSlot
from Model.Orm.OrmAnggota import OrmAnggota
from View.Component.QFrameComponent import QFrameComponent
from View.Component.QPushButtonComponent import QPushButtonComponent
from Class.Anggota import Anggota

class TableAnggota(QWidget):
    def __init__(self):
        super(TableAnggota,self).__init__()
        self.setWindowTitle("Data Anggota")
        self.setFixedSize(1000, 350)
        self.Ui()

    def Ui(self):
        self.buattabel()

    def buattabel(self):
        self.tableanggota = QTableWidget(self)
        self.tableanggota.cellClicked.connect(self.cek)
        self.tableanggota.setColumnCount(8)
        self.tableanggota.setHorizontalHeaderLabels(
            ["IdAnggota", "Nik", "Nama", "TempatLahir","TanggalLahir", "Alamat", "NoHandphone", "JenisKelamin"])
        self.tableanggota.setFixedSize(900, 350)
        self.tableanggota.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.isiTable()

    def cek(self, row):
        print(self.tableanggota.item(row, 0).text())
        print(self.tableanggota.item(row, 1).text())
        print(self.tableanggota.item(row, 2).text())
        print(self.tableanggota.item(row, 3).text())
        print(self.tableanggota.item(row, 4).text())
        print(self.tableanggota.item(row, 5).text())
        print(self.tableanggota.item(row, 6).text())
        print(self.tableanggota.item(row, 7).text())


    def isiTable(self):
        query = OrmAnggota.tampilanggota()
        self.tableanggota.setRowCount(len(query))
        for row in range(len(query)):
            self.tableanggota.setItem(row, 0, QTableWidgetItem(str(query[row].IdAnggota)))
            self.tableanggota.setItem(row, 1, QTableWidgetItem(str(query[row].Nik)))
            self.tableanggota.setItem(row, 2, QTableWidgetItem(query[row].Nama))
            self.tableanggota.setItem(row, 3, QTableWidgetItem(query[row].TempatLahir))
            self.tableanggota.setItem(row, 4, QTableWidgetItem(str(query[row].NoHandphone)))
            self.tableanggota.setItem(row, 5, QTableWidgetItem(query[row].TanggalLahir))
            self.tableanggota.setItem(row, 6, QTableWidgetItem(str(query[row].Alamat)))
            self.tableanggota.setItem(row, 7, QTableWidgetItem(str(query[row].JenisKelamin)))

    def simpan_btn(self):
        try:
            Anggota(self.text(),
                 self.nama.text(),
                 self.tempatlahir.text(),
                 self.tglLahir.text(),
                 self.alamat.toPlainText(),
                 self.nohp.text(),
                 self.jenkel.currentText())

            msg = QMessageBox()
            msg.setIcon(QMessageBox.Information)
            msg.setText("Data Telah Disimpan")
            msg.setWindowTitle("Berhasil")
            msg.exec_()
            self.isiTable()
        except Exception as e:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Information)

            msg.setText("Data tidak berhasil disimpan")
            msg.setInformativeText(f"ERROR : {e}")
            msg.setWindowTitle("Warning")
            msg.exec_()
def DataAnggotaView():
    app = QApplication(sys.argv)
    win = TableAnggota()
    win.show()
    sys.exit(app.exec_())

