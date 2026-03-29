from sqlalchemy import text
from sqlalchemy.orm import Session
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy import create_engine

from dotenv import load_dotenv
import os
import re

def create_db(name: str, link: str):

    if not re.fullmatch(r"[A-Za-z_][A-Za-z0-9_]*", name):
        raise ValueError("Nombre de base de datos no válido")

    temporal_engine = create_engine(link)

    sql = text(f"CREATE DATABASE IF NOT EXISTS `{name}`")

    with temporal_engine.connect() as conn:
        conn.execute(sql)
        conn.commit()
    

def getURL():
    load_dotenv()
    user = os.getenv('DB_USER')
    password = os.getenv('DB_PASSWORD')
    db_name = os.getenv('DB_NAME')

    first_link: str = f"mysql+pymysql://{user}:{password}@localhost"
    create_db(db_name, first_link)

    return f"mysql+pymysql://{user}:{password}@localhost/{db_name}"

def probar_conexion(session: Session) -> bool:
    try:
        session.execute(text("SELECT 1"))
        print("Conexion a la base de datos correcta")
        return True
    except SQLAlchemyError as e:
        print(f"Error de conexion: {e}")
        return False