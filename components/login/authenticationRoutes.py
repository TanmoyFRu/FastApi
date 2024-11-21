from fastapi import APIRouter, Depends, status, HTTPException
from fastapi.responses import JSONResponse
from fastapi.security import OAuth2PasswordRequestForm
from ..blog import blogModel
from .. import database
from ..utils.hashing import Hash
from sqlalchemy.orm import Session
from ..utils import token
from datetime import  timedelta

router = APIRouter(tags=['Authentication'])

@router.post('/login', status_code=status.HTTP_201_CREATED)
def login(request:OAuth2PasswordRequestForm = Depends(), db: Session = Depends(database.get_db)):
    user = db.query(blogModel.User).filter(blogModel.User.email == request.username).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Invalid Credentials")
    if not Hash.verify(str(user.password), request.password):
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Incorrect password")

    access_token = token.create_access_token(data={"sub": user.email})
    refresh_token = token.create_access_token(data={"sub": user.email},refresh= True, expires_delta=timedelta(days=2))
    return JSONResponse( content = {
        "access_token": access_token,
        "refresh_token" : refresh_token,
        "token_type": "bearer"
        }) 