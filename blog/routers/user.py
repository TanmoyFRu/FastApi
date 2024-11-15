
from sqlalchemy.orm import Session
from fastapi import APIRouter,Depends,status
from .. import schemas, database, oauth2
from ..repository import userRepository
router = APIRouter(
    prefix= "/user",
    tags = ["Users"]
)
get_db = database.get_db



@router.post('', response_model = schemas.Show_User)
def create_user(request : schemas.User, db: Session = Depends(get_db)):
    return userRepository.create(request,db)


@router.get('/{id}', response_model = schemas.Show_User, status_code=status.HTTP_200_OK)
def get_user_by_id(id: int, db: Session = Depends(get_db), current_user : schemas.User = Depends(oauth2.get_current_user)):
    return userRepository.get_all(id,db)