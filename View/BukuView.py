import sys
from PyQt5.QtGui import *
from PyQt5.QtCore import QDate
from PyQt5.QtWidgets import *
from View.Component.QPushButtonComponent import QPushButtonComponent
from Class.Buku import Buku
from Model.Orm.OrmBuku import OrmBuku


class BukuView(QWidget):

    def __init__(self):
        super(BukuView,self).__init__()
        self.setWindowTitle("Data Buku")
        self.resize(750, 350)
        self.UI()
        self.disableform()

    def UI(self):
        self.buatform()
        self.buattabelbuku()
        self.layoutUtama = QVBoxLayout()
        self.layouttabel = QHBoxLayout()
        self.layoutCrud = QHBoxLayout()

        self.btntambah = QPushButtonComponent("Tambah")
        self.btnedit = QPushButtonComponent("Edit")
        self.btnhapus = QPushButtonComponent("Hapus")

        self.layoutCrud.addWidget(self.btntambah)
        self.layoutCrud.addWidget(self.btnedit)
        self.layoutCrud.addWidget(self.btnhapus)
        self.layouttabel.addWidget(self.tablebuku)

        self.btntambah.clicked.connect(self.enableform)
        # self.btnedit.clicked.connect(lambda: self.editanggota())
        # self.btnhapus.clicked.connect(self.hapusAnggotaId)
        self.formbuku.addRow(self.layouttabel)
        self.formbuku.addRow(self.layoutCrud)

        self.layoutUtama.addLayout(self.layoutCrud)
        self.setLayout(self.layoutUtama)

    def buatform(self):
        # formlayout
        self.formbuku = QFormLayout(self)
        # data inputan

        self.judulb = QLineEdit(self)
        self.judulb.setPlaceholderText("Judul Buku")
        self.formbuku.addRow("Judul Buku        ", self.judulb)

        self.pengarang = QLineEdit(self)
        self.pengarang.setPlaceholderText("Pengarang")
        self.formbuku.addRow("Pengarang        ", self.pengarang)

        self.penerbit = QLineEdit(self)
        self.penerbit.setPlaceholderText("Penerbit")
        self.formbuku.addRow("Penerbit        ", self.penerbit)

        self.tahunterbit = QDateEdit(self)
        self.tahunterbit.setDisplayFormat('yyyy')
        self.tahunterbit.setDate(QDate.currentDate())
        self.formbuku.addRow("Tanggal Terbit        ", self.tahunterbit)

        self.stokbuku = QLineEdit(self)
        self.stokbuku.setPlaceholderText("Stok Buku")
        self.formbuku.addRow("Stok Buku         ", self.stokbuku)

        self.norak = QComboBox()
        self.norak.addItem("Drama")
        self.norak.addItem("Komedi")
        self.norak.addItem("Sejarah")
        self.norak.addItem("Biografi")
        self.formbuku.addRow("Rak           ", self.norak)
        # button
        self.btn_simpan = QPushButtonComponent("SIMPAN")
        self.btn_simpan.setFixedHeight(45)
        self.btn_simpan.clicked.connect(self.simpan_btn)
        self.formbuku.addRow(self.btn_simpan)

    def buattabelbuku(self):
        self.buattabel()

    def buattabel(self):
        self.tablebuku = QTableWidget()
        self.tablebuku.cellClicked.connect(self.isiForm)
        self.tablebuku.setColumnCount(7)
        self.tablebuku.setHorizontalHeaderLabels(
            ["IdBuku","Judul Buku","Pengarang", "Penerbit","Tahun Terbit", "Stok Buku", "No Rak"])
        self.tablebuku.setFixedSize(900, 350)
        self.tablebuku.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.isiTable()

    def isiTable(self):
        query = OrmBuku.tampilbuku()
        self.tablebuku.setRowCount(len(query))
        for row in range(len(query)):
            self.tablebuku.setItem(row, 0, QTableWidgetItem(str(query[row].IdBuku)))
            self.tablebuku.setItem(row, 1, QTableWidgetItem(str(query[row].JudulBuku)))
            self.tablebuku.setItem(row, 2, QTableWidgetItem(str(query[row].Pengarang)))
            self.tablebuku.setItem(row, 3, QTableWidgetItem(query[row].Penerbit))
            self.tablebuku.setItem(row, 4, QTableWidgetItem(query[row].TahunTerbit))
            self.tablebuku.setItem(row, 5, QTableWidgetItem(str(query[row].Stok)))
            self.tablebuku.setItem(row, 6, QTableWidgetItem(query[row].NomorRak))

    def isiForm(self, row):
        self.judulb.setText(self.tablebuku.item(row, 1).text())
        self.pengarang.setText(self.tablebuku.item(row, 2).text())
        self.penerbit.setText(self.tablebuku.item(row, 3).text())
        # self.tahunterbit.setDate(QDate(self.tablebuku.item(row, 4).text()))
        self.stokbuku.setText(self.tablebuku.item(row, 5).text())
        # self.nohp.setText(self.tableanggota.item(row, 6).text())
        #
        if str(self.tablebuku.item(row, 6).text()) == 'Drama':
            rak = 0
        elif str(self.tablebuku.item(row, 6).text()) == 'Komedi':
            rak = 1
        elif str(self.tablebuku.item(row, 6).text()) == 'Sejarah':
            rak = 1
        elif str(self.tablebuku.item(row, 6).text()) == 'Biografi':
            rak = 1
        self.norak.setCurrentIndex(rak)
    def simpan_btn(self):
        try:
            Buku(self.judulb.text(),
                    self.pengarang.text(),
                    self.penerbit.text(),
                    self.tahunterbit.text(),
                    self.stokbuku.text(),
                    self.norak.currentText())

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
        self.judulb.setReadOnly(True)
        self.pengarang.setReadOnly(True)
        self.penerbit.setReadOnly(True)
        self.tahunterbit.setDisabled(True)
        self.stokbuku.setReadOnly(True)
        self.norak.setDisabled(True)
        self.btn_simpan.setDisabled(True)

    def enableform(self):
        self.judulb.setReadOnly(False)
        self.pengarang.setReadOnly(False)
        self.penerbit.setReadOnly(False)
        self.tahunterbit.setDisabled(False)
        self.stokbuku.setReadOnly(False)
        self.norak.setDisabled(False)
        self.btn_simpan.setDisabled(False)
        self.judulb.setFocus()

    def refresh(self):
        self.judulb.clear()
        self.pengarang.clear()
        self.penerbit.clear()
        self.tahunterbit.clear()
        self.stokbuku.clear()


def tes():
    app = QApplication(sys.argv)
    win = BukuView()
    win.show()
    sys.exit(app.exec_())
