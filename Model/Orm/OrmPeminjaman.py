from sqlalchemy import Column, String, Integer, Text, Enum, Date,ForeignKey
from Model.base import Base, sessionFactory
from Model.Orm.OrmPengembalian import OrmPengembalian
from Class.StatusPinjam import StatusPinjam


class OrmPeminjaman(Base):
    __tablename__ = 'peminjaman'

    idpeminjaman = Column(Integer, primary_key=True)
    idanggota = Column(String)
    idpetugas = Column(String)
    idbuku = Column(String)
    tglPinjam = Column(String)
    tglKembali = Column(String)
    Status = Column(String)

    def __init__(self, idanggota, idpetugas, idbuku, tglPinjam, tglKembali, status):
        self.idanggota = idanggota
        self.idpetugas = idpetugas
        self.idbuku = idbuku
        self.tglPinjam = tglPinjam
        self.tglKembali = tglKembali
        self.Status = status
        session = sessionFactory()
        session.add(self)
        session.commit()
        session.close()


    @staticmethod
    def tambahPinjam():
        session = sessionFactory()
        pinjamORM = OrmPeminjaman(1, 1, 1, "Selesai")
        session.add(pinjamORM)
        kembaliORM = OrmPengembalian(1, 1, 1, "Selesai", "DuaRb")
        session.add(kembaliORM)
        session.commit()
        session.close()

    @staticmethod
    def tampilpinjam():
        session = sessionFactory()
        return session.query(OrmPeminjaman).all()
        session.close()

    def hapuspeminjaman(idSelect):
        session = sessionFactory()
        session.query(OrmPeminjaman).filter_by(idpeminjaman=idSelect).delete()
        session.commit()
        session.close()
