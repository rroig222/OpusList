from sqlalchemy import text
from sqlalchemy.orm import Session
from sqlalchemy.exc import SQLAlchemyError

def getURL():
    return "mysql+pymysql://root:root@localhost/OpusList"

def probar_conexion(session: Session) -> bool:
    try:
        session.execute(text("SELECT 1"))
        print("Conexion a la base de datos correcta")
        return True
    except SQLAlchemyError as e:
        print(f"Error de conexion: {e}")
        return False