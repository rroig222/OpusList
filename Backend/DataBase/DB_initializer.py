from sqlalchemy import create_engine
from sqlalchemy import Engine
from sqlalchemy.orm import declarative_base, sessionmaker, Session


from Backend.DataBase.DButil import getURL, probar_conexion

Base = declarative_base()

engine: Engine = create_engine(getURL(),echo=False)

SessionLocal = sessionmaker(bind=engine)
session: Session = SessionLocal()

print(probar_conexion(session=session))


