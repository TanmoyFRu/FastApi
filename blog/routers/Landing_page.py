from typing import List
from sqlalchemy.orm import Session
from fastapi import APIRouter,Depends,status,HTTPException,Response
from blog.hashing import Hash
from .. import schemas, database, models
router = APIRouter(
    tags = ["Landing Page"]
)
get_db = database.get_db

@router.get("/",status_code=status.HTTP_200_OK)
def Landing_page_blog():
    return 
f"Welcome to my Page Created By : Tanmoy Debnath"