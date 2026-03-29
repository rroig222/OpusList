from Backend.DataBase.DB_initializer import Base
from Backend.Models.UserWorkModel import UserWork
from Backend.Models.Composer.ComposerModel import Composer

from sqlalchemy import Column
from sqlalchemy import ForeignKey
from sqlalchemy import Integer
from sqlalchemy import Text
from sqlalchemy import String, Boolean
from sqlalchemy.orm import relationship
from sqlalchemy.ext.associationproxy import association_proxy


class Work(Base):

    __tablename__ = "works"

    id = Column(Integer, primary_key=True, autoincrement=True)
    title = Column(String(255), unique=True, nullable=False)
    genre = Column(String(255), nullable=False)
    openopus_id = Column(Integer, nullable=False, unique=True)

    composer_id = Column(Integer, ForeignKey("composers.id"))

    user_works = relationship("UserWork", back_populates="work")
    composer = relationship("Composer", back_populates="works")

    users = association_proxy("user_works", "user")

    def __repr__(self):
        return f"Work({self.id}, {self.title}, {self.composer})"