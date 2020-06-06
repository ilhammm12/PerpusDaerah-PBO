from PyQt5.QtWidgets import QGridLayout,QComboBox, QPushButton, QApplication, QAbstractItemView,QDialog, QMessageBox, QWidget, QHBoxLayout, QTableWidget, QTableWidgetItem, QVBoxLayout
import sys
from PyQt5.QtCore import Qt, pyqtSlot
from Model.Orm.OrmPengunjung import OrmPengunjung
from View.Component.QFrameComponent import QFrameComponent
from View.Component.QPushButtonComponent import QPushButtonComponent

class TablePengunjung(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Data Petugas")
        self.setFixedSize(1000, 350)
        self.Ui()

    def Ui(self):
        self.buattabel()
        self.layoutUtama = QGridLayout()

        self.btntambah = QPushButtonComponent("Tambah")


        self.btntambah.clicked.connect(lambda: self.formpengunjung())
        frameCrudSection = QFrameComponent("white")
        frameCrudSection.setContentsMargins(5, 5, 5, 5)
        self.layoutUtama = QGridLayout()


        frameCrudSection = QFrameComponent("white")
        frameCrudSection.setContentsMargins(5, 5, 5, 5)
        frameTabel = QFrameComponent("white")
        frameTabel.setContentsMargins(5, 5, 5, 5)

        layoutCrudSection = QHBoxLayout(frameCrudSection)
        layoutTabel = QVBoxLayout(frameTabel)
        self.layoutUtama.addWidget(frameCrudSection, 1, 0, 2, 9, Qt.AlignTop)
        self.layoutUtama.addWidget(frameTabel, 5, 0, 3, 9, Qt.AlignBottom)

        layoutCrudSection.addWidget(self.btntambah)



        layoutTabel.addWidget(self.table)
        self.setLayout(self.layoutUtama)
        self.show()

    def buattabel(self):
        self.table = QTableWidget()
        self.table.cellClicked.connect(self.cek)
        self.table.setColumnCount(5)
        self.table.setHorizontalHeaderLabels(
            ["Id Pengunjung","Nama","Alamat","NoHandphone","Tanggal Berkunjung"])
        self.table.setFixedSize(900, 350)
        self.table.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.isiTable()

    def cek(self, row):
        print(self.table.item(row, 0).text())
        print(self.table.item(row, 1).text())
        print(self.table.item(row, 2).text())
        print(self.table.item(row, 3).text())
        print(self.table.item(row, 4).text())

    def isiTable(self):
        query = OrmPengunjung.tampilpengunjung()
        self.table.setRowCount(len(query))
        for row in range(len(query)):
            self.table.setItem(row, 0, QTableWidgetItem(str(query[row].IdPengunjung)))
            self.table.setItem(row, 1, QTableWidgetItem(str(query[row].Nama)))
            self.table.setItem(row, 2, QTableWidgetItem(str(query[row].Alamat)))
            self.table.setItem(row, 3, QTableWidgetItem(query[row].NoHp))
            self.table.setItem(row, 4, QTableWidgetItem(query[row].TanggalBerkunjung))


    def formpengunjung(self):
        from View.PengunjungView import FormPengunjungView
        self.pengunjungview = FormPengunjungView()
        self.pengunjungview.show()
        self.pengunjungview.exec_()


def DataAnggotaView():
    app = QApplication(sys.argv)
    win = TablePengunjung()
    win.show()
    sys.exit(app.exec_())

DataAnggotaView()