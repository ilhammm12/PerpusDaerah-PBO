from Class.Peminjaman import Peminjaman

class Pengembalian():

    def __init__(self, denda):
        self.__denda = denda

    @property
    def denda(self):
        return self.__denda

    @denda.setter
    def denda(self, denda):
        self.__denda = denda

