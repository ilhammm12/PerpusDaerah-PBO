from Model.base import sessionFactory
from Model.Orm.OrmPeminjaman import OrmPeminjaman
from Class.Anggota import Anggota
from Class.Petugas import Petugas
from Class.Buku import Buku
from Model.Orm.OrmPeminjaman import OrmPeminjaman

class Peminjaman():
    def __init__(self, IdAnggota, IdPetugas, IdBuku , tanggalPinjam, tanggalKembali, status):
        self.__IdAnggota = IdAnggota
        self.__IdPetugas = IdPetugas
        self.__IdBuku = IdBuku
        self.__tanggalPinjam = tanggalPinjam
        self.__tanggalKembali = tanggalKembali
        self.__status = status
        self.insertpinjam()

    def insertpinjam(self):
        OrmPeminjaman(self.__IdAnggota,
                       self.__IdPetugas,
                       self.__IdBuku,
                       self.__tanggalPinjam,
                       self.__tanggalKembali,
                       self.__status)

    @property
    def tanggalPinjam(self):
        return self.__tanggalPinjam
    @tanggalPinjam.setter
    def tanggalPinjam(self, value):
        self.__tanggalPinjam = value

    @property
    def tanggalKembalig(self):
        return self.__tanggalKembali
    @tanggalKembalig.setter
    def tanggalKembalig(self, value):
        self.__tanggalKembali = value

    @property
    def status(self):
        return self.__status
    @status.setter
    def status(self, value):
        self.__status = value

# x = Peminjaman("1","1","1","02/05/2020","12/07/2020","Dipinjam")
