from PyQt5.QtWidgets import QGridLayout,QComboBox, QPushButton, QApplication, QAbstractItemView,QDialog, QMessageBox, QWidget, QHBoxLayout, QTableWidget, QTableWidgetItem, QVBoxLayout
import sys
from PyQt5.QtCore import Qt, pyqtSlot
from Model.Orm.OrmBuku import OrmBuku
from View.Component.QFrameComponent import QFrameComponent
from View.Component.QPushButtonComponent import QPushButtonComponent

class TableBuku(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Data Buku")
        self.setFixedSize(1000, 350)
        self.Ui()

    def Ui(self):
        self.buattabel()
        self.layoutUtama = QGridLayout()

        self.btntambah = QPushButtonComponent("Tambah")
        self.btnedit = QPushButtonComponent("Edit")
        self.btnhapus = QPushButtonComponent("Hapus")

        self.btntambah.clicked.connect(lambda: self.formbuku())

        frameCrudSection = QFrameComponent("white")
        frameCrudSection.setContentsMargins(5, 5, 5, 5)
        frameTabel = QFrameComponent("white")
        frameTabel.setContentsMargins(5, 5, 5, 5)

        layoutCrudSection = QHBoxLayout(frameCrudSection)
        layoutTabel = QVBoxLayout(frameTabel)
        self.layoutUtama.addWidget(frameCrudSection, 1, 0, 2, 9, Qt.AlignTop)
        self.layoutUtama.addWidget(frameTabel, 5, 0, 3, 9, Qt.AlignBottom)

        layoutCrudSection.addWidget(self.btntambah)
        layoutCrudSection.addWidget(self.btnedit)
        layoutCrudSection.addWidget(self.btnhapus)


        layoutTabel.addWidget(self.table)
        self.setLayout(self.layoutUtama)
        self.show()

    def buattabel(self):
        self.table = QTableWidget()
        self.table.cellClicked.connect(self.cek)
        self.table.setColumnCount(6)
        self.table.setHorizontalHeaderLabels(
            ["IdBuku","Pengarang", "Penerbit","Tahun Terbit", "Stok Buku", "No Rak"])
        self.table.setFixedSize(900, 350)
        self.table.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.isiTable()

    def cek(self, row):
        print(self.table.item(row, 0).text())
        print(self.table.item(row, 1).text())
        print(self.table.item(row, 2).text())
        print(self.table.item(row, 3).text())
        print(self.table.item(row, 4).text())
        print(self.table.item(row, 5).text())


    def isiTable(self):
        query = OrmBuku.tampilbuku()
        self.table.setRowCount(len(query))
        for row in range(len(query)):
            self.table.setItem(row, 0, QTableWidgetItem(str(query[row].IdBuku)))
            self.table.setItem(row, 1, QTableWidgetItem(str(query[row].Pengarang)))
            self.table.setItem(row, 2, QTableWidgetItem(query[row].Penerbit))
            self.table.setItem(row, 3, QTableWidgetItem(query[row].TahunTerbit))
            self.table.setItem(row, 4, QTableWidgetItem(str(query[row].Stok)))
            self.table.setItem(row, 5, QTableWidgetItem(query[row].NomorRak))


    def formbuku(self):
        from View.BukuView import FormBukuView
        self.anggotaview = FormBukuView()
        self.anggotaview.show()
        self.anggotaview.exec_()


def DataAnggotaView():
    app = QApplication(sys.argv)
    win = TableBuku()
    win.show()
    sys.exit(app.exec_())

DataAnggotaView()