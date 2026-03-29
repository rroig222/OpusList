from Backend.DataBase.DB_initializer import Base
#from Backend.Models.User.UserModel import User
#from Backend.Models.Work.WorkModel import Work


from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship


class UserWork(Base):
    __tablename__ = "user_work"

    user_id = Column(Integer, ForeignKey("users.id"), primary_key=True)
    work_id = Column(Integer, ForeignKey("works.id"), primary_key=True)
    rating = Column(Integer)

    user = relationship("User", back_populates="user_works")
    work = relationship("Work", back_populates="user_works")