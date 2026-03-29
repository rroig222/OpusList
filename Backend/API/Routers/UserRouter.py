from fastapi import APIRouter, HTTPException, Depends, status
from Backend.Models.User.UserService import UserService
from Backend.Models.Work.WorkService import WorkService

from pydantic import EmailStr
from Backend.Schemas.UserSchemas import GetUser, NewUser, LoginUser, RateWork, UserWorks, RatingResponse
from Backend.API.dependencies import get_user_service, get_work_service


router = APIRouter(prefix="/users", tags=["Users"])

@router.post("/new",response_model=GetUser, status_code=201)
async def create_user(data: NewUser,
                      user_service: UserService = Depends(get_user_service)):
    
    try:
        user = user_service.create_user_service(data.username, data.email, data.password)
        return user

    # Error usuario ya existe
    except ValueError as e:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail=str(e))

@router.post("/login", response_model=GetUser, status_code=status.HTTP_202_ACCEPTED)
async def login_check(data: LoginUser,
                      user_service: UserService = Depends(get_user_service)):
    
    try:
        user = user_service.check_user_login_service(username=data.username, password=data.password)
        return user

    except ValueError as e:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=str(e))

@router.post("/rate", response_model=RateWork, status_code=status.HTTP_200_OK)
async def rate_work(data: RateWork,
                    user_service: UserService = Depends(get_user_service),
                    work_service: WorkService = Depends(get_work_service)):

    user = user_service.userCRUD.search_user_by_id(data.user_id)
    work = work_service.workCRUD.get_work_by_id(data.work_id)

    if not user or not work:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"NOT FOUND (User: {user}, Work: {work})")

    user_service.rate_work_service(work=work, user=user, rating=data.rating)

    return data

@router.get("/id/{id}", response_model=GetUser, status_code=status.HTTP_200_OK)
async def get_user(id: int,
                   user_service: UserService = Depends(get_user_service)):
    
    user = user_service.userCRUD.search_user_by_id(id=id)

    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"User {id} not found!")
    
    return user

@router.get("/works/{id}", response_model=UserWorks, status_code=status.HTTP_200_OK)
async def get_user_works(id: int,
                         user_service: UserService = Depends(get_user_service)):
    
    user = user_service.userCRUD.search_user_by_id(id=id)

    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"User {id} not found!")
    
    output = {'id': id,
              'username': user.username,
              'email': user.email,
              'works': user.works}
    
    return output

@router.get("/rate/{work_id}/{user_id}", response_model=RatingResponse, status_code=status.HTTP_200_OK)
async def get_rating(work_id: int,
                     user_id:int,
                     user_service: UserService = Depends(get_user_service),
                     work_service: WorkService = Depends(get_work_service)):
    
    user = user_service.userCRUD.search_user_by_id(user_id)
    work = work_service.workCRUD.get_work_by_id(id=work_id)

    if not user:
        raise HTTPException(status_code=404, detail=f"User with id = {user_id} not found")
    if not work:
        raise HTTPException(status_code=404, detail=f"Work with id= {work_id} not found")

    else:
        rating = user_service.userCRUD.get_rating_by_user_and_work(user=user, work=work)
        return {"rating": rating}