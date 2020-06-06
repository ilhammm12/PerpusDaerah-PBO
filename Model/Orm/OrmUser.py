from sqlalchemy import Column, String, Integer, Enum


from Model.base import Base, sessionFactory
from Class.HakAkses import HakAkses

class OrmUser(Base):
    __tablename__ = 'tbl_user'

    id_username = Column(Integer, primary_key=True)
    username = Column(String, unique=True)
    password = Column(String)
    hak_akses = Column(Enum(HakAkses))

    def __init__(self, username, password, HakAkses):
        self.username = username
        self.password = password
        self.hak_akses = HakAkses
        session = sessionFactory()
        session.add(self)
        session.commit()
        session.close()

    @staticmethod
    def insertUser():
        session = sessionFactory()
        userOrm = OrmUser("Ilhamm","ilham123","Admin")
        session.add(userOrm)
        session.commit()
        session.close()

    @staticmethod
    def hapusUser(username):
        try:
            session = sessionFactory()
            session.query(OrmUser).filter_by(username=username).delete()
            session.commit()
            session.close()
        except Exception as e:
            print("===>", e)
        else:
            print("Data telah Berhasil Dihapus")

    @staticmethod
    def tampiluser():
        session = sessionFactory()
        return session.query(OrmUser).all()
        session.close()

    @staticmethod
    def cekuser(username, password) -> bool:
        try:
            session = sessionFactory()
            if ((session.query(OrmUser).filter_by(username=username, password=password).count()) == 1):
                return True
            else:
                return False
            session.close()
        except Exception as e:
            print("===>", e)

    @staticmethod
    def findHakAkses(username):
        try:
            session = sessionFactory()
            for user in session.query(OrmUser).filter_by(username=username):
                return user.hak_akses
            session.close()
        except Exception as e:
            print("===>", e)
