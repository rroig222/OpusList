from fastapi import APIRouter, HTTPException, Depends, status
from Backend.Models.User.UserService import UserService
from Backend.Models.Work.WorkService import WorkService
from Backend.Models.Composer.ComposerService import ComposerService

from pydantic import EmailStr
from Backend.Schemas.UserSchemas import GetUser, NewUser, LoginUser, RateWork, UserWorks
from Backend.Schemas.ComposerSchemas import GetComposer
from Backend.API.dependencies import get_user_service, get_work_service, get_composer_service


router = APIRouter(prefix="/composers", tags=["Composers"])

@router.get("/{id}", response_model=GetComposer, status_code=status.HTTP_200_OK)
async def get_composer_by_id(id: int,
                             composer_service: ComposerService = Depends(get_composer_service)):
    try:
        composer = composer_service.get_composer_by_id_db(id)
    except ValueError as e:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Composer with id = {id} not found")

    return composer