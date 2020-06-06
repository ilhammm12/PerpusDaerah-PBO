from Model.Orm.OrmPetugas import OrmPetugas

class Petugas():

    def __init__(self, nama, tempatLahir, tanggalLahir, alamat, nohandphone, jenisKelamin):
        self.__nama = nama
        self.__tempatLahir = tempatLahir
        self.__tanggalLahir = tanggalLahir
        self.__alamat = alamat
        self.__nohandphone = nohandphone
        self.__jenisKelamin = jenisKelamin
        self.insertpetugas()

    def insertpetugas(self):
        OrmPetugas(self.__nama,
                   self.__tempatLahir,
                   self.__tanggalLahir,
                   self.__alamat,
                   self.__nohandphone,
                   self.__jenisKelamin)

    @property
    def nama(self):
        return self.__nama


    @nama.setter
    def nama(self, nama):
        self.__nama = nama


    @property
    def tempatLahir(self):
        return self.__tempatLahir


    @tempatLahir.setter
    def tempatLahir(self, tempatLahir):
        self.__tempatLahir = tempatLahir


    @property
    def tanggalLahir(self):
        return self.__tanggalLahir


    @tanggalLahir.setter
    def tanggalLahir(self, tanggalLahir):
        self.__tanggalLahir = tanggalLahir


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


    @property
    def jenisKelamin(self):
        return self.__jenisKelamin

    @jenisKelamin.setter
    def jenisKelamin(self, jenisKelamin):
        self.__jenisKelamin = jenisKelamin

