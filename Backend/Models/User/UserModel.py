from Backend.DataBase.DB_initializer import Base
from Backend.Models.UserWorkModel import UserWork

from sqlalchemy import Column
from sqlalchemy import ForeignKey
from sqlalchemy import Integer
from sqlalchemy import Text
from sqlalchemy import String, Boolean
from sqlalchemy.orm import relationship

from sqlalchemy.ext.associationproxy import association_proxy


class User(Base):

    __tablename__ = "users"

    id = Column(Integer, primary_key=True, autoincrement=True, unique=True)
    username = Column(String(55), unique=True, nullable=False)
    email = Column(String(55), unique=True, nullable=False)
    password_hash = Column(String(255), nullable=False)

    user_works = relationship("UserWork", back_populates="user")

    works = association_proxy("user_works", "work")

    def __repr__(self):
        return f"User({self.id},{self.username})"
