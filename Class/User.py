from Model.Orm.OrmUser import OrmUser

class User():

    def __init__(self, username, password, hak_akses):
        self.__Username = username
        self.__Password = password
        self.__HakAkses = hak_akses
        self.insertuser()

    def insertuser(self):
        OrmUser(self.__Username,
                   self.__Password,
                   self.__HakAkses)

    @property
    def username(self):
        return self.__Username

    @username.setter
    def username(self, username):
        self.__Username = username

    @property
    def password(self):
        return self.__Password

    @password.setter
    def password(self, password):
        self.__Password = password

    @property
    def hak_akses(self):
        return self.__HakAkses

    @hak_akses.setter
    def hak_akses(self, hak_akses):
        self.__HakAkses = hak_akses

