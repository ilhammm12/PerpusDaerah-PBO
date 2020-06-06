import sys

from PyQt5 import QtCore
from PyQt5.QtWidgets import *

from View.Component.QFrameComponent import QFrameComponent
from View.Component.QPushButtonComponent import QPushButtonComponent


class MainMenuView(QWidget):
    def __init__(self):
        super().__init__()

        self.showMaximized()
        self.setWindowFlag(QtCore.Qt.WindowCloseButtonHint, False)
        self.setWindowTitle("MENU")


        frameheadBar = QFrameComponent("white")


        headBarLayout = QGridLayout(frameheadBar)
        headBarLayout.setSpacing(5)

        self.btnPetugas = QPushButtonComponent("Data Petugas")
        self.btnAnggota = QPushButtonComponent("Data Anggota")
        self.btnTransaksi = QPushButtonComponent("Transaksi")
        self.btnBuku = QPushButtonComponent("Data Buku")
        self.btnUser = QPushButtonComponent("Data User")
        self.btnLogOut = QPushButtonComponent("Log Out")

        framebodybar = QFrameComponent("maroon")
        bodyBarLayout = QHBoxLayout(framebodybar)


        headBarLayout.addWidget(self.btnPetugas, 0,1)
        headBarLayout.addWidget(self.btnAnggota, 0, 2)
        headBarLayout.addWidget(self.btnBuku, 0, 3)
        headBarLayout.addWidget(self.btnTransaksi, 0, 4)
        headBarLayout.addWidget(self.btnUser, 0, 5)
        headBarLayout.addWidget(self.btnLogOut, 0, 6, QtCore.Qt.AlignBottom)


        layoutUtama = QGridLayout()
        layoutUtama.addWidget(frameheadBar,0, 1, 1, 10, QtCore.Qt.AlignTop)
        layoutUtama.addWidget(framebodybar,2,1,1,10)

        self.btnPetugas.clicked.connect(lambda: self.openpetugas())
        self.btnAnggota.clicked.connect(lambda: self.openanggota())
        self.btnBuku.clicked.connect(lambda: self.openbuku())
        self.btnUser.clicked.connect(lambda: self.openuser())
        self.btnTransaksi.clicked.connect(lambda: self.openpeminjaman())
        self.btnLogOut.clicked.connect(lambda: self.openlogout())
        # self.hak_akses()
        self.setLayout(layoutUtama)
        self.show()




    def openpetugas(self):
        from View.PetugasView import PetugasView
        self.petugasview = PetugasView()
        self.petugasview.show()


    def openanggota(self):
        from View.AnggotaView import AnggotaView
        self.anggotaview = AnggotaView()
        self.anggotaview.show()


    def openbuku(self):
        from View.BukuView import BukuView
        self.bukuview = BukuView()
        self.bukuview.show()

    def openuser(self):
        from View.UserView import UserView
        self.userview =UserView()
        self.userview.show()


    def openpeminjaman(self):
        from View.PeminjamanView import PeminjamanView
        self.pinjamview = PeminjamanView()
        self.pinjamview.show()

    #
    # def openpengembalian(self):
    #     from View.PengembalianView import PengembalianView
    #     self.kembaliview = PengembalianView()
    #     self.kembaliview.show()
    #     self.kembaliview.exec_()
    #

    #
    def openlogout(self):
        from View.LoginView import LoginView
        self.loginview = LoginView()
        self.loginview.show()
        self.close()

    # def hak_akses(self):
    #     HakAkses = self.HakAkses.text()
    #     if (HakAkses == str(HakAkses.PETUGAS)):
    #         self.btnPetugas.setVisible(False)
    #         self.btnUser.setVisible(False)
    #     elif (HakAkses == str(HakAkses.ADMIN)):
    #         self.btnPetugas.setVisible(True)
    #         self.btnUser.setVisible(True)

