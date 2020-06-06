import sys

from PyQt5.QtWidgets import *
from View.Component.QPushButtonComponent import QPushButtonComponent
from Class.Petugas import Petugas
from Model.Orm.OrmPetugas import OrmPetugas

class PetugasView(QWidget):

    def __init__(self):
        super(PetugasView,self).__init__()
        self.setWindowTitle("Data Petugas")
        self.resize(750, 350)
        self.UI()
        self.disableform()

    def UI(self):
        self.buatform()
        self.buattabelpetugas()
        self.layoutUtama = QVBoxLayout()
        self.layouttabel = QHBoxLayout()
        self.layoutCrud = QHBoxLayout()

        self.btntambah = QPushButtonComponent("Tambah")
        self.btnedit = QPushButtonComponent("Edit")
        self.btnhapus = QPushButtonComponent("Hapus")

        self.layoutCrud.addWidget(self.btntambah)
        self.layoutCrud.addWidget(self.btnedit)
        self.layoutCrud.addWidget(self.btnhapus)
        self.layouttabel.addWidget(self.tablepetugas)

        self.btntambah.clicked.connect(self.enableform)
        # self.btnedit.clicked.connect(lambda: self.editanggota())
        self.btnhapus.clicked.connect(self.hapusAnggotaId)
        self.formpetugas.addRow(self.layouttabel)
        self.formpetugas.addRow(self.layoutCrud)

        self.layoutUtama.addLayout(self.layoutCrud)
        self.setLayout(self.layoutUtama)

    def buatform(self):
        # formlayout
        self.formpetugas = QFormLayout(self)
        # data inputan

        self.nama = QLineEdit(self)
        self.nama.setPlaceholderText("Nama Petugas")
        self.formpetugas.addRow("Nama Petugas", self.nama)

        self.tempatlahir = QLineEdit(self)
        self.tempatlahir.setPlaceholderText("Tempat Lahir")
        self.formpetugas.addRow("Tempat Lahir", self.tempatlahir)

        self.tglLahir = QDateEdit(self)
        self.tglLahir.setDisplayFormat('dd/MM/yyyy')
        self.tglLahir.setCalendarPopup(True)
        self.formpetugas.addRow("Tanggal Lahir", self.tglLahir)

        self.alamat = QTextEdit(self)
        self.alamat.setPlaceholderText("Alamat")
        self.alamat.setFixedHeight(50)
        self.formpetugas.addRow("Alamat", self.alamat)

        self.nohp = QLineEdit(self)
        self.nohp.setInputMask("+62 9999 9999 999")
        self.formpetugas.addRow("No Handphone", self.nohp)

        self.jenkel = QComboBox()
        self.jenkel.addItem("laki-laki")
        self.jenkel.addItem("perempuan")
        self.formpetugas.addRow("Jenis Kelamin ", self.jenkel)
        # button
        self.btn_simpan = QPushButtonComponent("SIMPAN")
        self.btn_simpan.setFixedHeight(45)
        self.btn_simpan.clicked.connect(self.simpan_btn)
        self.formpetugas.addRow(self.btn_simpan)

    def buattabelpetugas(self):
        self.buattabel()

    def buattabel(self):
        self.tablepetugas = QTableWidget()
        self.tablepetugas.cellClicked.connect(self.cek)
        self.tablepetugas.setColumnCount(7)
        self.tablepetugas.setHorizontalHeaderLabels(
            ["IdPetugas", "Nama", "TempatLahir", "TanggalLahir", "Alamat", "NoHandphone", "JenisKelamin"])
        self.tablepetugas.setFixedSize(900, 350)
        self.tablepetugas.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.isiTable()

    def cek(self, row):
        print(self.tablepetugas.item(row, 0).text())
        print(self.tablepetugas.item(row, 1).text())
        print(self.tablepetugas.item(row, 2).text())
        print(self.tablepetugas.item(row, 3).text())
        print(self.tablepetugas.item(row, 4).text())
        print(self.tablepetugas.item(row, 5).text())
        print(self.tablepetugas.item(row, 6).text())

    def isiTable(self):
        query = OrmPetugas.tampilpetugas()
        self.tablepetugas.setRowCount(len(query))
        for row in range(len(query)):
            self.tablepetugas.setItem(row, 0, QTableWidgetItem(str(query[row].idpetugas)))
            self.tablepetugas.setItem(row, 1, QTableWidgetItem(str(query[row].Nama)))
            self.tablepetugas.setItem(row, 2, QTableWidgetItem(query[row].TempatLahir))
            self.tablepetugas.setItem(row, 3, QTableWidgetItem(query[row].TanggalLahir))
            self.tablepetugas.setItem(row, 4, QTableWidgetItem(str(query[row].Alamat)))
            self.tablepetugas.setItem(row, 5, QTableWidgetItem(query[row].NoHandphone))
            self.tablepetugas.setItem(row, 6, QTableWidgetItem(str(query[row].JenisKelamin)))

    def simpan_btn(self):
        try:
            Petugas(self.nama.text(),
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
        self.tempatlahir.setReadOnly(True)
        self.tglLahir.setReadOnly(True)
        self.alamat.setReadOnly(True)
        self.nohp.setReadOnly(True)
        self.jenkel.setDisabled(True)
        self.btn_simpan.setDisabled(True)

    def enableform(self):
        self.nama.setReadOnly(False)
        self.tempatlahir.setReadOnly(False)
        self.tglLahir.setReadOnly(False)
        self.alamat.setReadOnly(False)
        self.nohp.setReadOnly(False)
        self.jenkel.setDisabled(False)
        self.btn_simpan.setDisabled(False)
        self.nama.setFocus()

    def refresh(self):
        self.nama.clear()
        self.tempatlahir.clear()
        self.tglLahir.clear()
        self.alamat.clear()
        self.nohp.clear()

    def cekid(self, row):
        self.SelectedId = int(self.tablepetugas.item(row, 0).text())
        print(self.SelectedId)

    def hapusAnggotaId(self, row):
        SelectedId = int(self.tablepetugas.item(row, 0).text())
        OrmPetugas.hapusPetugas(SelectedId)
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Information)
        msg.setText("Data Telah Dihapus")
        msg.setWindowTitle("Berhasil")
        msg.exec_()
        self.isiTable()
