from sqlalchemy.orm import Session
from ..blog import blogModel
from . import userSchema
from fastapi import HTTPException,status
from ..utils.hashing import Hash



def create(request : userSchema.User, db : Session):
    new_user = blogModel.User(name = request.name, email = request.email, password = Hash.bcrypt(request.password))
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user

def get_all(id:int, db : Session):
    user = db.query(blogModel.User).filter(blogModel.User.id == id).first()
    if not user : 
       raise HTTPException(status_code = status.HTTP_404_NOT_FOUND, detail = f"Blog with the id {id} is not available")
    return user