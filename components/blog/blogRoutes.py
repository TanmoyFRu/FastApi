from typing import List
from sqlalchemy.orm import Session
from fastapi import APIRouter,Depends,status
from ..user import userSchema
from ..utils import oauth2
from .. import database
from . import blogRepository
 
 
router = APIRouter(
    prefix = "/blog",
    tags=["Blogs"]
)
get_db = database.get_db


@router.get("", response_model=List[userSchema.Show_Blog],status_code=status.HTTP_200_OK)
def get_all_blog(db: Session = Depends(get_db), current_user : userSchema.User = Depends(oauth2.get_current_user)):
    return blogRepository.get_all(db)

@router.post('', status_code=status.HTTP_201_CREATED)
def create_blog(request: userSchema.Blog, db: Session = Depends(get_db), current_user : userSchema.User = Depends(oauth2.get_current_user)):
    return blogRepository.create(request, db)

@router.delete("/{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_blog_by_id(id: int, db: Session = Depends(get_db), current_user : userSchema.User = Depends(oauth2.get_current_user)):
    return blogRepository.delete(id,db)  

@router.get('/{id}', status_code=status.HTTP_200_OK, response_model=userSchema.Show_Blog)
def get_blog_by_id(id: int,db: Session = Depends(get_db), current_user : userSchema.User = Depends(oauth2.get_current_user)):
     return blogRepository.show(id,db)

@router.put('/{id}', status_code = status.HTTP_202_ACCEPTED)
def update_blog_by_id(id: int, request: userSchema.Blog, db: Session = Depends(get_db), current_user : userSchema.User = Depends(oauth2.get_current_user)):
    return blogRepository.update(id,db,request)