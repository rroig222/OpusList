from fastapi import APIRouter, HTTPException, Depends, status
from Backend.Models.User.UserService import UserService
from Backend.Models.Work.WorkService import WorkService

from Backend.Models.Work.WorkModel import Work

import json

from pydantic import EmailStr
from Backend.Schemas.UserSchemas import GetUser, NewUser, LoginUser
from Backend.Schemas.WorkSchemas import GetWork, WorkSearchDB, WorkSearchedDB, WorkSearchedOpenOpus
from Backend.API.dependencies import get_user_service, get_work_service


router = APIRouter(prefix="/works", tags=["Works"])

@router.get("/openopus/{id}", response_model=GetWork, status_code=status.HTTP_201_CREATED)
async def create_work_by_openopus_id(id: int,
                                     work_service: WorkService = Depends(get_work_service)):
    
    try:
        work = work_service.import_work_from_openopus_by_id_service(openopus_id=id)


    except ValueError as e:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Work not found!")
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Unkown error!")

    return work

@router.get("/{id}", response_model=GetWork, status_code=status.HTTP_202_ACCEPTED)
async def get_work(id: int,
                   work_service: WorkService = Depends(get_work_service)):

    work = work_service.workCRUD.get_work_by_id(id=id)

    if not work:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Work not found!")
    
    return work

@router.get("/search-db/{user_id}/{query}", response_model=WorkSearchDB)
async def search_works_db(query: str,
                          user_id: int,
                          work_service: WorkService = Depends(get_work_service)):
    
    works = work_service.search_work_in_db(query=query)
    user = work_service.userCRUD.search_user_by_id(id=user_id)

    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found")

    if not works:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Works not found")

    final_works: list = []

    for work_tuple in works:
        work_searched = WorkSearchedDB(work=work_tuple[0], 
                                       matched_by=work_tuple[1], 
                                       rating=work_service.userCRUD.get_rating_by_user_and_work(user, work_tuple[0]))
        
        final_works.append(work_searched)
    
    return WorkSearchDB(works=final_works)

@router.get("/openopus/{composer}/{query}", response_model=WorkSearchedOpenOpus)
def get_work_openopus(composer: str,
                      query: str,
                      work_service: WorkService = Depends(get_work_service)):
    
    try:
        works: list[Work] = work_service.search_work_in_openopus(composer=composer, query=query)
        return {'works': works}
    
    except LookupError as e:
        raise HTTPException(status_code=404, detail=str(e))
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
    except ConnectionError as e:
        raise HTTPException(status_code=502, detail=str(e))
