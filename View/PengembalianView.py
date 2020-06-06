import sys

from PyQt5.QtWidgets import *
from PyQt5.QtCore import QDate
from Model.Orm.OrmPengembalian import OrmPengembalian
from View.Component.QPushButtonComponent import QPushButtonComponent
from Class.Pengembalian import Pengembalian

class PengembalianView(QWidget):

    def __init__(self):
        super(PengembalianView,self).__init__()
        self.setWindowTitle("Data Pengembalian Buku")
        self.resize(750, 350)
        self.UI()
        self.disableform()

    def UI(self):
        self.buatform()
        self.buattabelpinjam()
        self.layoutUtama = QVBoxLayout()
        self.layouttabel = QHBoxLayout()
        self.layoutCrud = QHBoxLayout()

        self.btntambah = QPushButtonComponent("Tambah")
        self.btnedit = QPushButtonComponent("Edit")
        self.btnhapus = QPushButtonComponent("Hapus")


        self.layoutCrud.addWidget(self.btntambah)
        self.layoutCrud.addWidget(self.btnedit)
        self.layoutCrud.addWidget(self.btnhapus)

        self.layouttabel.addWidget(self.tablepinjam)

        self.btntambah.clicked.connect(self.enableform)
        # self.btnedit.clicked.connect(lambda: self.editanggota())
        # self.btnhapus.clicked.connect(self.hapusAnggotaId)
        self.formpinjam.addRow(self.layouttabel)
        self.formpinjam.addRow(self.layoutCrud)

        self.layoutUtama.addLayout(self.layoutCrud)
        self.setLayout(self.layoutUtama)


    def buatform(self):
        # formlayout
        self.formpinjam = QFormLayout(self)
        # data inputan

        self.idpinjam = QLineEdit(self)
        self.idpinjam.setPlaceholderText("Id Peminjaman")
        self.formpinjam.addRow("Id Peminjaman      ", self.idpinjam)

        self.idanggota = QLineEdit(self)
        self.idanggota.setPlaceholderText("Id Anggota")
        self.formpinjam.addRow("Id Anggota      ", self.idanggota)

        self.idpetugas = QLineEdit(self)
        self.idpetugas.setPlaceholderText("Id Petugas")
        self.formpinjam.addRow("Id Petugas      ", self.idpetugas)

        self.idbuku= QLineEdit(self)
        self.idbuku.setPlaceholderText("Id Buku")
        self.formpinjam.addRow("Id Buku     ", self.idbuku)

        self.tglpinjam = QDateEdit(self)
        self.tglpinjam.setDisplayFormat('dd/MM/yyyy')
        self.tglpinjam.setCalendarPopup(True)
        self.formpinjam.addRow("Tanggal Peminjaman      ", self.tglpinjam)

        self.tglkembali = QDateEdit(self)
        self.tglkembali.setDisplayFormat('dd/MM/yyyy')
        self.tglkembali.setCalendarPopup(True)
        self.formpinjam.addRow("Tanggal Kembalikan       ", self.tglkembali)

        self.tgldikembali = QDateEdit(self)
        self.tgldikembali.setDisplayFormat('dd/MM/yyyy')
        self.tgldikembali.setCalendarPopup(True)
        self.tgldikembali.setDate(QDate.currentDate())
        self.formpinjam.addRow("Tanggal Dikembalikan      ", self.tgldikembali)

        self.status = QComboBox()
        self.status.addItem("Dipinjam")
        self.status.addItem("Selesai")
        self.formpinjam.addRow("Status      ", self.status)

        self.denda = QComboBox()
        self.denda.addItem("NolRb")
        self.denda.addItem("DuaRb")
        self.denda.addItem("LimaRb")
        self.formpinjam.addRow("Denda      ", self.denda)

        # button
        self.btn_simpan = QPushButtonComponent("SIMPAN")
        self.btn_simpan.setFixedHeight(45)
        self.btn_simpan.clicked.connect(self.simpan_btn)
        self.formpinjam.addRow(self.btn_simpan)


    def buattabelpinjam(self):
        self.buattabel()

    def buattabel(self):
        self.tablepinjam = QTableWidget(self)

        self.tablepinjam.setColumnCount(9)
        self.tablepinjam.setHorizontalHeaderLabels(
            ["Id Pengembalian","Id Peminjaman", "Id Anggota", "Id Petugas", "Id Buku", "Tanggal Peminjaman", "Tanggal Kembalikan","Tanggal Dikembalikan", "Status"])
        self.tablepinjam.setFixedSize(900, 350)
        self.tablepinjam.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.isiTable()

    def isiTable(self):
        query = OrmPengembalian.tampilpengembaian()

        self.tablepinjam.setRowCount(len(query))
        for row in range(len(query)):
            self.tablepinjam.setItem(row, 0, QTableWidgetItem(str(query[row].idpengembalian)))
            self.tablepinjam.setItem(row, 1, QTableWidgetItem(str(query[row].idpeminjaman)))
            self.tablepinjam.setItem(row, 2, QTableWidgetItem(str(query[row].idanggota)))
            self.tablepinjam.setItem(row, 3, QTableWidgetItem(str(query[row].idpetugas)))
            self.tablepinjam.setItem(row, 4, QTableWidgetItem(str(query[row].idbuku)))
            self.tablepinjam.setItem(row, 5, QTableWidgetItem(str(query[row].tglPinjam)))
            self.tablepinjam.setItem(row, 6, QTableWidgetItem(str(query[row].tglKembali)))
            self.tablepinjam.setItem(row, 7, QTableWidgetItem(str(query[row].tglDikembalikan)))
            self.tablepinjam.setItem(row, 8, QTableWidgetItem(str(query[row].Status)))
            self.tablepinjam.setItem(row, 9, QTableWidgetItem(str(query[row].Denda)))




    def simpan_btn(self):
        try:

            Pengembalian(self.idpinjam.text(),
                    self.idanggota.text(),
                    self.idpetugas.text(),
                    self.idbuku.text(),
                    self.tglpinjam.text(),
                    self.tglkembali.text(),
                    self.tgldikembali.text(),
                    self.status.currentText(),
                    self.denda.currentText())

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
        self.idpinjam.setReadOnly(True)
        self.idanggota.setReadOnly(True)
        self.idpetugas.setReadOnly(True)
        self.idbuku.setReadOnly(True)
        self.tglpinjam.setReadOnly(True)
        self.tglkembali.setReadOnly(True)
        self.tgldikembali.setReadOnly(True)
        self.status.setDisabled(True)
        self.denda.setDisabled(True)
        self.btn_simpan.setDisabled(True)

    def enableform(self):
        self.idpinjam.setReadOnly(False)
        self.idanggota.setReadOnly(False)
        self.idpetugas.setReadOnly(False)
        self.idbuku.setReadOnly(False)
        self.tglpinjam.setReadOnly(False)
        self.tglkembali.setReadOnly(False)
        self.tgldikembali.setReadOnly(False)
        self.status.setDisabled(False)
        self.denda.setDisabled(False)
        self.btn_simpan.setDisabled(False)
        self.idpinjam.setFocus()

    def refresh(self):
        self.idpinjam.clear()
        self.idanggota.clear()
        self.idpetugas.clear()
        self.idbuku.clear()


