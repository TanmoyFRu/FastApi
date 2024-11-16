from fastapi import APIRouter,status
from . import database
router = APIRouter(
    tags = ["Landing Page"]
)
get_db = database.get_db

@router.get("/",status_code=status.HTTP_200_OK)
def Landing_page():
    return 
f"Welcome to my Page Created By : Tanmoy Debnath"