
from sqlalchemy.orm import Session
from fastapi import APIRouter,Depends,status

from ..utils import oauth2
from .. import database
from . import userRepository, userSchema
router = APIRouter(
    prefix= "/user",
    tags = ["Users"]
)
get_db = database.get_db



@router.post('', response_model = userSchema.Show_User,status_code=status.HTTP_201_CREATED)
def create_user(request : userSchema.User, db: Session = Depends(get_db)):
    return userRepository.create(request,db)


@router.get('/{id}', response_model = userSchema.Show_User, status_code=status.HTTP_200_OK)
def get_user_by_id(id: int, db: Session = Depends(get_db), current_user : userSchema.User = Depends(oauth2.get_current_user)):
    return userRepository.get_all(id,db)