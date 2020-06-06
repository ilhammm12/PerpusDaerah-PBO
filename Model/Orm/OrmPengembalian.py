from sqlalchemy import Column, String, Integer, Text, Enum, Date,ForeignKey
from Model.base import Base, sessionFactory

from Class.StatusPinjam import StatusPinjam
from Class.Denda import Denda

class OrmPengembalian(Base):
    __tablename__ = 'tb_pengembalian'

    idpengembalian = Column(Integer, primary_key=True)
    idpeminjaman = Column(String)
    idanggota = Column(String)
    idpetugas = Column(String)
    idbuku = Column(String)
    tglPinjam = Column(String)
    tglKembali = Column(String)
    tglDikembalikan = Column(String)
    Status = Column(String)
    Denda = Column(String)

    def __init__(self,idpeminjaman,idanggota, idpetugas, idbuku,tglPinjam,tglKembali, tglDikembalikan, status,denda):
        self.idpeminjaman = idpeminjaman
        self.idanggota = idanggota
        self.idpetugas = idpetugas
        self.idbuku = idbuku
        self.tglPinjam = tglPinjam
        self.tglKembali = tglKembali
        self.tglDikembalikan =tglDikembalikan
        self.Status = status
        self.Denda = denda
        session = sessionFactory()
        session.add(self)
        session.commit()
        session.close()

    @staticmethod
    def hapusKembali():
        session = sessionFactory()
        session.query(OrmPengembalian).filter_by(Status="Selesai").delete()
        session.commit()
        session.close()

    @staticmethod
    def jumlahkembali():
        return sessionFactory().query(OrmPengembalian).filter_by(Status="Selesai").count()

    @staticmethod
    def tampilpengembaian():
        session = sessionFactory()
        return session.query(OrmPengembalian).all()
        session.close()

    def hapuspengembalian(idSelect):
        session = sessionFactory()
        session.query(OrmPengembalian).filter_by(idpengembalian=idSelect).delete()
        session.commit()
        session.close()
