from pydantic import BaseModel
from typing import List, Optional


class BlogBase(BaseModel):
    title:str
    body:str

class Blog(BlogBase):
    class Config():
       orm_mode = True

class User(BaseModel):
    name : str 
    email : Optional[str] = None
    password: str
    

class Show_User(BaseModel):
    name : str 
    email : str
    blogs : List[Blog] = [] 
    
    class Config():
        orm_mode = True
        
        
class Show_Blog(BaseModel):
    title : str
    body : str
    creator: Show_User
    
    class Config():
        orm_mode = True
        
class Login(BaseModel):
    username : str
    password : str