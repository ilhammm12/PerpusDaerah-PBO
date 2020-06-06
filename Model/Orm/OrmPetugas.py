from sqlalchemy import create_engine, Column, Integer, String, Enum,Date
from Model.base import Base, sessionFactory
from Class.JenisKelamin import JenisKelamin


class OrmPetugas(Base):

    __tablename__ = 'tb_petugas'

    idpetugas = Column(Integer, primary_key=True)
    Nama = Column(String)
    TempatLahir = Column(String)
    TanggalLahir = Column(String)
    Alamat = Column(String)
    NoHandphone = Column(String)
    JenisKelamin = Column(String)

    def __init__(self, nama, tempatlahir,tanggallahir, alamat, nohandphone, jeniskelamin):
        self.Nama = nama
        self.TempatLahir = tempatlahir
        self.TanggalLahir = tanggallahir
        self.Alamat = alamat
        self.NoHandphone = nohandphone
        self.JenisKelamin = jeniskelamin
        session = sessionFactory()
        session.add(self)
        session.commit()
        session.close()

    # @staticmethod
    # def tambahPetugas():
    #     session = sessionFactory()
    #     petugasORM = OrmPetugas("Wahyu","Paser","Giri",821,"lakilaki")
    #     session.add(petugasORM)
    #     session.commit()
    #     session.close()

    @staticmethod
    def editPetugas():
        session = sessionFactory()
        session.query(OrmPetugas).filter_by(idpetugas=1).update({
        OrmPetugas.Nama: "Wahyu Achmad Shafardan"
        }, synchronize_session=False)
        session.commit()
        session.close()

    @staticmethod
    def hapusPetugas():
        session = sessionFactory()
        session.query(OrmPetugas).filter_by(idpetugas=1).delete()
        session.commit()
        session.close()

    @staticmethod
    def tampilpetugas():
        session = sessionFactory()
        return session.query(OrmPetugas).all()
        session.close()

