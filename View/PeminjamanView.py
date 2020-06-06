import sys

from PyQt5.QtWidgets import *
from PyQt5.QtCore import QDate
from Model.Orm.OrmPeminjaman import OrmPeminjaman
from View.Component.QPushButtonComponent import QPushButtonComponent
from Class.Peminjaman import Peminjaman

class PeminjamanView(QWidget):

    def __init__(self):
        super(PeminjamanView,self).__init__()
        self.setWindowTitle("Data Peminjaman Buku")
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
        self.btnkembali = QPushButtonComponent("Kembalikan Buku")

        self.layoutCrud.addWidget(self.btntambah)
        self.layoutCrud.addWidget(self.btnedit)
        self.layoutCrud.addWidget(self.btnhapus)
        self.layoutCrud.addWidget(self.btnkembali)
        self.layouttabel.addWidget(self.tablepinjam)

        self.btntambah.clicked.connect(self.enableform)
        # self.btnedit.clicked.connect(lambda: self.editanggota())
        self.btnhapus.clicked.connect(self.hapusid)
        self.btnkembali.clicked.connect(self.kembalikanbuku)
        self.formpinjam.addRow(self.layouttabel)
        self.formpinjam.addRow(self.layoutCrud)

        self.layoutUtama.addLayout(self.layoutCrud)
        self.setLayout(self.layoutUtama)


    def buatform(self):
        # formlayout
        self.formpinjam = QFormLayout(self)
        # data inputan
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
        self.tglpinjam.setDate(QDate.currentDate())
        self.formpinjam.addRow("Tanggal Peminjaman      ", self.tglpinjam)

        self.tglkembali = QDateEdit(self)
        self.tglkembali.setDisplayFormat('dd/MM/yyyy')
        self.tglkembali.setCalendarPopup(True)
        self.formpinjam.addRow("Tanggal Kembalikan       ", self.tglkembali)

        self.status = QComboBox()
        self.status.addItem("Dipinjam")
        self.status.addItem("Selesai")
        self.formpinjam.addRow("Status      ", self.status)

        # button
        self.btn_simpan = QPushButtonComponent("SIMPAN")
        self.btn_simpan.setFixedHeight(45)
        self.btn_simpan.clicked.connect(self.simpan_btn)
        self.formpinjam.addRow(self.btn_simpan)


    def buattabelpinjam(self):
        self.buattabel()

    def buattabel(self):
        self.tablepinjam = QTableWidget(self)

        self.tablepinjam.setColumnCount(7)
        self.tablepinjam.setHorizontalHeaderLabels(
            ["Id Peminjaman", "Id Anggota", "Id Petugas", "Id Buku", "Tanggal Peminjaman", "Tanggal Kembalikan", "Status"])
        self.tablepinjam.setFixedSize(900, 350)
        self.tablepinjam.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.isiTable()

    def isiTable(self):
        query = OrmPeminjaman.tampilpinjam()

        self.tablepinjam.setRowCount(len(query))
        for row in range(len(query)):
            self.tablepinjam.setItem(row, 0, QTableWidgetItem(str(query[row].idpeminjaman)))
            self.tablepinjam.setItem(row, 1, QTableWidgetItem(str(query[row].idanggota)))
            self.tablepinjam.setItem(row, 2, QTableWidgetItem(str(query[row].idpetugas)))
            self.tablepinjam.setItem(row, 3, QTableWidgetItem(str(query[row].idbuku)))
            self.tablepinjam.setItem(row, 4, QTableWidgetItem(str(query[row].tglPinjam)))
            self.tablepinjam.setItem(row, 5, QTableWidgetItem(str(query[row].tglKembali)))
            self.tablepinjam.setItem(row, 6, QTableWidgetItem(str(query[row].Status)))


    def simpan_btn(self):
        try:

            Peminjaman(self.idanggota.text(),
                    self.idpetugas.text(),
                    self.idbuku.text(),
                    self.tglpinjam.text(),
                    self.tglkembali.text(),
                    self.status.currentText())

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


    def kembalikanbuku(self):
        from View.PengembalianView import PengembalianView
        self.kembalikan = PengembalianView()
        self.kembalikan.show()


    def disableform(self):
        self.idanggota.setReadOnly(True)
        self.idpetugas.setReadOnly(True)
        self.idbuku.setReadOnly(True)
        self.tglpinjam.setReadOnly(True)
        self.tglkembali.setReadOnly(True)
        self.status.setDisabled(True)
        self.btn_simpan.setDisabled(True)

    def enableform(self):
        self.idanggota.setReadOnly(False)
        self.idpetugas.setReadOnly(False)
        self.idbuku.setReadOnly(False)
        self.tglpinjam.setReadOnly(False)
        self.tglkembali.setReadOnly(False)

        self.btn_simpan.setDisabled(False)
        self.idanggota.setFocus()

    def refresh(self):
        self.idanggota.clear()
        self.idpetugas.clear()
        self.idbuku.clear()

    def cekid(self, row):
        self.SelectedId = int(self.tablepinjam.item(row, 0).text())
        print(self.SelectedId)

    def hapusid(self, row):
        SelectedId = int(self.tablepinjam.item(row, 0).text())
        OrmPeminjaman.hapuspeminjaman(SelectedId)
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Information)
        msg.setText("Data Telah Dihapus")
        msg.setWindowTitle("Berhasil")
        msg.exec_()
        self.isiTable()

def tes():
    app = QApplication(sys.argv)
    win = PeminjamanView()
    win.show()
    sys.exit(app.exec_())

