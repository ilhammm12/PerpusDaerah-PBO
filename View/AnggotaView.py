import sys

from PyQt5.QtWidgets import *
from Model.Orm.OrmAnggota import OrmAnggota
from View.Component.QPushButtonComponent import QPushButtonComponent
from Class.Anggota import Anggota


class AnggotaView(QWidget):

    def __init__(self):
        super(AnggotaView,self).__init__()
        self.setWindowTitle("Data Anggota")
        self.resize(750, 350)
        self.UI()
        self.disableform()
        self.SelectedId=None

    def UI(self):
        self.buatform()
        self.buattabelanggota()
        self.layoutUtama = QVBoxLayout()
        self.layouttabel = QHBoxLayout()
        self.layoutCrud = QHBoxLayout()

        self.btntambah = QPushButtonComponent("Tambah")
        self.btnedit = QPushButtonComponent("Edit")
        self.btnhapus = QPushButtonComponent("Hapus")

        self.layoutCrud.addWidget(self.btntambah)
        self.layoutCrud.addWidget(self.btnedit)
        self.layoutCrud.addWidget(self.btnhapus)
        self.layouttabel.addWidget(self.tableanggota)

        self.btntambah.clicked.connect(self.enableform)
        self.btnedit.clicked.connect(lambda: self.editanggota())
        self.btnhapus.clicked.connect(self.hapusAnggotaId)
        self.formanggota.addRow(self.layouttabel)
        self.formanggota.addRow(self.layoutCrud)

        # self.layoutUtama.addLayout(self.layouttabel)
        self.layoutUtama.addLayout(self.layoutCrud)
        self.setLayout(self.layoutUtama)


    def buatform(self):
        # formlayout
        self.formanggota = QFormLayout(self)
        # data inputan
        self.Nik = QLineEdit(self)
        self.Nik.setPlaceholderText("Nomor Induk Keluarga")
        self.formanggota.addRow("NIK", self.Nik)

        self.nama = QLineEdit(self)
        self.nama.setPlaceholderText("Nama Anggota")
        self.formanggota.addRow("Nama Anggota", self.nama)

        self.tempatlahir = QLineEdit(self)
        self.tempatlahir.setPlaceholderText("Tempat Lahir")
        self.formanggota.addRow("Tempat Lahir", self.tempatlahir)

        self.tglLahir = QDateEdit(self)
        self.tglLahir.setDisplayFormat('dd/MM/yyyy')
        self.tglLahir.setCalendarPopup(True)
        self.formanggota.addRow("Tanggal Lahir", self.tglLahir)

        self.alamat = QTextEdit(self)
        self.alamat.setPlaceholderText("Alamat")
        self.alamat.setFixedHeight(50)
        self.formanggota.addRow("Alamat", self.alamat)

        self.nohp = QLineEdit(self)
        self.nohp.setInputMask("+62 9999 9999 999")
        self.formanggota.addRow("No Handphone", self.nohp)

        self.jenkel = QComboBox()
        self.jenkel.addItem("laki-laki")
        self.jenkel.addItem("perempuan")
        self.formanggota.addRow("Jenis Kelamin ", self.jenkel)
        # button
        self.btn_simpan = QPushButtonComponent("SIMPAN")
        self.btn_simpan.setFixedHeight(45)
        self.btn_simpan.clicked.connect(self.simpan_btn)
        self.formanggota.addRow(self.btn_simpan)


    def buattabelanggota(self):
        self.buattabel()

    def buattabel(self):
        self.tableanggota = QTableWidget(self)
        self.tableanggota.cellClicked.connect(self.cekid)
        self.tableanggota.setColumnCount(8)
        self.tableanggota.setHorizontalHeaderLabels(
            ["IdAnggota", "Nik", "Nama", "TempatLahir", "TanggalLahir", "Alamat", "NoHandphone", "JenisKelamin"])
        self.tableanggota.setFixedSize(900, 350)
        self.tableanggota.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.isiTable()

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

            Anggota(self.Nik.text(),
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

    def cekid(self, row):
        self.SelectedId = int(self.tableanggota.item(row, 0).text())
        print(self.SelectedId)

    def hapusAnggotaId(self):
        if self.SelectedId != None:
            OrmAnggota.hapusAnggota(self.SelectedId)
            self.isiTable()

    def disableform(self):
        self.Nik.setReadOnly(True)
        self.nama.setReadOnly(True)
        self.tempatlahir.setReadOnly(True)
        self.tglLahir.setReadOnly(True)
        self.alamat.setReadOnly(True)
        self.nohp.setReadOnly(True)
        self.jenkel.setDisabled(True)
        self.btn_simpan.setDisabled(True)

    def enableform(self):
        self.Nik.setReadOnly(False)
        self.nama.setReadOnly(False)
        self.tempatlahir.setReadOnly(False)
        self.tglLahir.setReadOnly(False)
        self.alamat.setReadOnly(False)
        self.nohp.setReadOnly(False)
        self.jenkel.setDisabled(False)
        self.btn_simpan.setDisabled(False)
        self.Nik.setFocus()

    def refresh(self):
        self.Nik.clear()
        self.nama.clear()
        self.tempatlahir.clear()
        self.tglLahir.clear()
        self.alamat.clear()
        self.nohp.clear()


    def hapusAnggotaId(self, row):
        SelectedId = int(self.tableanggota.item(row, 0).text())
        OrmAnggota.hapusAnggota(SelectedId)
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Information)
        msg.setText("Data Telah Dihapus")
        msg.setWindowTitle("Berhasil")
        msg.exec_()
        self.isiTable()

def tes():
    app = QApplication(sys.argv)
    win = AnggotaView()
    win.show()
    sys.exit(app.exec_())