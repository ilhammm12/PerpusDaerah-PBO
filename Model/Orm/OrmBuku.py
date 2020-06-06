from sqlalchemy import Column, String, Integer, Text, Enum, Date
from Model.base import Base, sessionFactory

class OrmBuku(Base):
    __tablename__ = "tb_buku"

    IdBuku = Column(Integer, primary_key=True)
    JudulBuku = Column(String, unique=True)
    Pengarang = Column(String)
    Penerbit = Column(String)
    TahunTerbit = Column(String)
    Stok = Column(String)
    NomorRak = Column(String)

    def __init__(self, judulbuku, pengarang, penerbit, tahunterbit, stok, nomorrak):
        self.JudulBuku = judulbuku
        self.Pengarang = pengarang
        self.Penerbit = penerbit
        self.TahunTerbit = tahunterbit
        self.Stok = stok
        self.NomorRak = nomorrak
        session = sessionFactory()
        session.add(self)
        session.commit()
        session.close()

    @staticmethod
    def tambahBuku():
        session = sessionFactory()
        bukuOrm = OrmBuku("Kambing Borneo","Radidtya","Gramedia","2017",50,1)
        session.add(bukuOrm)
        session.commit()
        session.close()

    @staticmethod
    def editBuku():
        session = sessionFactory()
        session.query(OrmBuku).filter_by(IdBuku=1).update({
            OrmBuku.NomorRak:"Komedi"}, synchronize_session=False)
        session.commit()
        session.close()

    @staticmethod
    def hapusBuku():
        session = sessionFactory()
        session.query(OrmBuku).filter_by(IdBuku=1).delete()
        session.commit()
        session.close()

    @staticmethod
    def tampilbuku():
        session = sessionFactory()
        return session.query(OrmBuku).all()
        session.close()

    def hapusBuku(idSelect):
        session = sessionFactory()
        session.query(OrmBuku).filter_by(IdBuku=idSelect).delete()
        session.commit()
        session.close()
