from sqlalchemy import Column, String, Integer, Text, Enum, Date
from sqlalchemy.orm import relationships
from Class.JenisKelamin import JenisKelamin
from Model.base import Base, sessionFactory

class OrmPengunjung(Base):
    __tablename__ = 'tb_pengunjung'

    IdPengunjung = Column(Integer,primary_key=True)
    Nama = Column(String, unique = True)
    Alamat = Column(String)
    NoHp = Column(String)
    TanggalBerkunjung = Column(String)

    def __init__(self,Nama,Alamat, NoHp,TanggalBerkunjung):
        self.Nama = Nama
        self.Alamat = Alamat
        self.NoHp = NoHp
        self.TanggalBerkunjung = TanggalBerkunjung
        session = sessionFactory()
        session.add(self)
        session.commit()
        session.close()

    @staticmethod
    def tambahAnggota():
        session = sessionFactory()
        pengunjungORM = OrmPengunjung("Irfan","lakilaki",628424)
        session.add(pengunjungORM)
        session.commit()
        session.close()

    @staticmethod
    def jumlahkembali():
        return sessionFactory().query(OrmPengunjung).count()

    @staticmethod
    def tampilpengunjung():
        session = sessionFactory()
        return session.query(OrmPengunjung).all()
        session.close()
# print(OrmPengunjung.jumlahkembali())
# OrmPengunjung.tambahAnggota()
