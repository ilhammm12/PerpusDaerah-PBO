from sqlalchemy import Column, String, Integer, Text, Enum, Date,ForeignKey
from Model.base import Base, sessionFactory

from Class.StatusPinjam import StatusPinjam
from Class.Denda import Denda

class OrmPengembalian(Base):
    __tablename__ = 'tb_pengembalian'

    idpengembalian = Column(Integer, primary_key=True)
    idanggota = Column(Integer)
    idpetugas = Column(Integer)
    idbuku = Column(Integer)
    #tglPinjam = Column(Date)
    #tglKembali = Column(Date)
    Status = Column(Enum(StatusPinjam))
    Denda = Column(Enum(Denda))

    def __init__(self,idanggota, idpetugas, idbuku, status,denda):
        self.idanggota = idanggota
        self.idpetugas = idpetugas
        self.idbuku = idbuku
         #self.tglPinjam = tglPinjam
         #self.tglKembali = tglKembali
        self.Status = status
        self.Denda = denda

    @staticmethod
    def hapusKembali():
        session = sessionFactory()
        session.query(OrmPengembalian).filter_by(Status="Selesai").delete()
        session.commit()
        session.close()

    @staticmethod
    def jumlahkembali():
        return sessionFactory().query(OrmPengembalian).filter_by(Status="Selesai").count()

