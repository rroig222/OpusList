from Backend.DataBase.DB_initializer import Base
#from Backend.Models.Work.WorkModel import Work

from sqlalchemy import Column
from sqlalchemy import ForeignKey
from sqlalchemy import Integer
from sqlalchemy import Text
from sqlalchemy import String, Boolean
from sqlalchemy.orm import relationship
from sqlalchemy.ext.associationproxy import association_proxy


class Composer(Base):

    __tablename__ = "composers"

    id = Column(Integer, primary_key=True, autoincrement=True, unique=True)
    openopus_id = Column(Integer, unique=True, nullable=False)
    name = Column(String(255), nullable=False)
    complete_name = Column(String(255), nullable=False)
    epoch = Column(String(255), nullable=False)

    works = relationship("Work", back_populates="composer")

    def __repr__(self):
        return f"Composer({self.id}, {self.complete_name})"