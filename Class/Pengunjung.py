from Model.Orm.OrmPengunjung import OrmPengunjung

class Pengunjung():

    def __init__(self, nama, alamat, nohandphone, tanggalberkunjung):
        self.__nama = nama
        self.__alamat = alamat
        self.__nohandphone = nohandphone
        self.__tanggalberkunjung = tanggalberkunjung
        self.insertpengunjung()

    def insertpengunjung(self):
        OrmPengunjung(self.__nama,
                   self.__alamat,
                   self.__nohandphone,
                   self.__tanggalberkunjung)

    @property
    def nama(self):
        return self.__nama

    @nama.setter
    def nama(self, nama):
        self.__nama = nama

    @property
    def alamat(self):
        return self.__alamat

    @alamat.setter
    def alamat(self, alamat):
        self.__alamat = alamat

    @property
    def nohandphone(self):
        return self.__nohandphone

    @nohandphone.setter
    def nohandphone(self, nohandphone):
        self.__nohandphone = nohandphone

