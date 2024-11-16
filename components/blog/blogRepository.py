from sqlalchemy.orm import Session

from . import blogModel
from .. import schemas
from fastapi import HTTPException,status,Response


def get_all(db:Session):
    blogs = db.query(blogModel.Blog).all()
    return blogs

def create(request :schemas.Blog,db : Session):
    new_blog = blogModel.Blog(title=request.title, body=request.body, user_id = 1)
    db.add(new_blog)
    db.commit()
    db.refresh(new_blog)
    return new_blog

def delete(id : int,db : Session):
    blog = db.query(blogModel.Blog).filter(blogModel.Blog.id == id)
    if not blog.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Blog with id {id} not found")
    blog.delete(synchronize_session=False)
    db.commit()
    return Response(status_code=status.HTTP_204_NO_CONTENT) 

def update(id: int , db : Session, request:schemas.Blog):
     blog_to_update = db.query(blogModel.Blog).filter(blogModel.Blog.id == id).first()
     if not blog_to_update:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Blog with ID {id} not found")
     for key, value in request.dict().items():
        setattr(blog_to_update, key, value)
     db.commit()
     return f"ID {id} Updated Successfully"
 
def show(id:int,db : Session):
    blog_to_get = db.query(blogModel.Blog).filter(blogModel.Blog.id == id).first()
    if not blog_to_get:
       raise HTTPException(status_code = status.HTTP_404_NOT_FOUND, detail = f"Blog with the id {id} is not available")
    return blog_to_get