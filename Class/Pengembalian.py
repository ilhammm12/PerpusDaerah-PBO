from Class.Peminjaman import Peminjaman
from Model.Orm.OrmPengembalian import OrmPengembalian

class Pengembalian():

    def __init__(self,idpeminjaman,IdAnggota, IdPetugas, IdBuku, tanggalPinjam, tanggalKembali,tanggalDikembalikan,status,denda):
            self.__idPeminjaman = idpeminjaman
            self.__IdAnggota = IdAnggota
            self.__IdPetugas = IdPetugas
            self.__IdBuku = IdBuku
            self.__tanggalPinjam = tanggalPinjam
            self.__tanggalKembali = tanggalKembali
            self.__tanggalDikembalikan = tanggalDikembalikan
            self.__status = status
            self.__denda = denda
            self.insertpinjam()


    def insertpinjam(self):
        OrmPengembalian(self.__idPeminjaman,
                       self.__IdAnggota,
                       self.__IdPetugas,
                       self.__IdBuku,
                       self.__tanggalPinjam,
                       self.__tanggalKembali,
                       self.__tanggalDikembalikan,
                       self.__status,
                       self.__denda)



    @property
    def denda(self):
        return self.__denda

    @denda.setter
    def denda(self, denda):
        self.__denda = denda

x = Pengembalian("1","1","1","1","02/05/2020","12/07/2020","17/07/2020","Dipinjam","LimaRb")
