from typing import List
from fastapi import FastAPI, Depends, status,HTTPException,Response
from blog import schemas, models
# " . " means from the same directory
from sqlalchemy.orm import Session
from blog.database import engine, SessionLocal
from passlib.context import CryptContext


app = FastAPI()

models.Base.metadata.create_all(bind=engine)



def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()



@app.get("/")
def Landing_page_blog():
    return "Welcome to my Blog"



@app.get("/blog", response_model=List[schemas.Show_Blog])
def get_all_blog(db: Session = Depends(get_db)):
    blogs = db.query(models.Blog).all()
    return blogs



@app.post('/blog', status_code=status.HTTP_201_CREATED)
def create_blog(request: schemas.Blog, db: Session = Depends(get_db)):
    new_blog = models.Blog(title=request.title, body=request.body)
    db.add(new_blog)
    db.commit()
    db.refresh(new_blog)
    return new_blog



@app.delete("/blog/{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_blog_by_id(id: int, db: Session = Depends(get_db)):
    blog = db.query(models.Blog).filter(models.Blog.id == id)
    if not blog.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Blog with id {id} not found")
    blog.delete(synchronize_session=False)
    db.commit()
    return Response(status_code=status.HTTP_204_NO_CONTENT)   


 
@app.get('/blog/{id}', status_code=status.HTTP_200_OK, response_model=schemas.Show_Blog)
def get_blog_by_id(id: int, response : Response,db: Session = Depends(get_db)):
    blog_to_get = db.query(models.Blog).filter(models.Blog.id == id).first()
    if not blog_to_get:
       raise HTTPException(status_code = status.HTTP_404_NOT_FOUND, detail = f"Blog with the id {id} is not available")
    return blog_to_get



@app.put('/blog/{id}', status_code = status.HTTP_202_ACCEPTED)
def update_blog_by_id(id: int, request: schemas.Blog, db: Session = Depends(get_db)):
    blog_to_update = db.query(models.Blog).filter(models.Blog.id == id).first()
    if not blog_to_update:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Blog with ID {id} not found")
    for key, value in request.dict().items():
        setattr(blog_to_update, key, value)
    db.commit()
    return f"ID {id} Updated Successfully"



pwd_cxt = CryptContext(schemes = ['bcrypt'], deprecated = 'auto')


@app.post('/user')
def create_user(request : schemas.User, db: Session = Depends(get_db)):
    hashedPassword = pwd_cxt.hash(request.password)
    new_user = models.User(**request.model_dump())
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user
h1