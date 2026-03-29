from fastapi import Depends
from typing import Generator
from Backend.DataBase.DB_initializer import SessionLocal
from sqlalchemy.orm import Session

from Backend.Models.Work.WorkCRUD import WorkCRUD
from Backend.Models.Work.WorkService import WorkService
from Backend.Models.User.UserCRUD import UserCRUD
from Backend.Models.User.UserService import UserService
from Backend.Models.Composer.ComposerCRUD import ComposerCRUD
from Backend.Models.Composer.ComposerService import ComposerService

def get_session() -> Generator[Session, None, None]:
    session = SessionLocal()
    try:
        yield session
    finally:
        session.close()


# CRUD
def get_userCRUD(session: Session = Depends(get_session)) -> UserCRUD:
    return UserCRUD(session)

def get_composerCRUD(session: Session = Depends(get_session)) -> ComposerCRUD:
    return ComposerCRUD(session=session)

def get_workCRUD(session: Session = Depends(get_session)) -> WorkCRUD:
    return WorkCRUD(session)


# Services
def get_composer_service(userCRUD: UserCRUD = Depends(get_userCRUD), 
                         workCRUD: WorkCRUD = Depends(get_workCRUD), 
                         composerCRUD: ComposerCRUD = Depends(get_composerCRUD)) -> ComposerService:
    return ComposerService(userCRUD=userCRUD,workCRUD=workCRUD,composerCRUD=composerCRUD)

def get_user_service(userCRUD: UserCRUD = Depends(get_userCRUD)) -> UserService:
    return UserService(userCRUD=userCRUD)

def get_work_service(userCRUD: UserCRUD = Depends(get_userCRUD), 
                     workCRUD: WorkCRUD = Depends(get_workCRUD),
                     composerCRUD: ComposerCRUD = Depends(get_composerCRUD),
                     composer_service: ComposerService = Depends(get_composer_service)) -> WorkService:
    return WorkService(userCRUD=userCRUD, workCRUD=workCRUD, composer_service=composer_service, composerCRUD=composerCRUD)

