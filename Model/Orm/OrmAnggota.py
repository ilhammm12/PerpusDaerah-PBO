from sqlalchemy import Column, String, Integer, Text, Date
from sqlalchemy.orm import relationships
from Model.base import Base, sessionFactory

class OrmAnggota(Base):
    __tablename__ = 'anggota'

    IdAnggota = Column(Integer,primary_key=True)
    Nik = Column(String, unique = True)
    Nama = Column(String)
    TempatLahir = Column(String)
    TanggalLahir = Column(String)
    Alamat = Column(String)
    NoHandphone = Column(String)
    JenisKelamin = Column(String)


    def __init__(self,nik, nama, tempatlahir,tanggallahir, alamat, nohandphone, jeniskelamin):

        self.Nik = nik
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


    @staticmethod
    def editAnggota():
        session = sessionFactory()
        session.query(OrmAnggota).filter_by(Nik =1181089).update({
         OrmAnggota.JenisKelamin:"perempuan"
        }, synchronize_session=False)
        session.commit()
        session.close()

    def hapusAnggota(idAnggotaSelect):
        session = sessionFactory()
        session.query(OrmAnggota).filter_by(IdAnggota=idAnggotaSelect).delete()
        session.commit()
        session.close()

    @staticmethod
    def tampilAnggota():
        try:
            session = sessionFactory()
            # hasil = []
            for Anggota in session.query(OrmAnggota).all():
                print("Nik = {} \n Nama = {}".format(Anggota.Nik, Anggota.JenisKelamin))
                # hasil.append([str(Anggota.IdAnggota),str(Anggota.Nik), str(Anggota.Nama), str(Anggota.TempatLahir),str(Anggota.Alamat), str(Anggota.NoHandphone), str(Anggota.JenisKelamin)])

                # return hasil
                session.close()
        except Exception as e:
            print("===>", e)

    @staticmethod
    def tampilanggota():
        session = sessionFactory()
        return session.query(OrmAnggota).all()
        session.close()

