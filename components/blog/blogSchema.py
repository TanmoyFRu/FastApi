from pydantic import BaseModel

    
class BlogBase(BaseModel):
    title:str
    body:str

class Blog(BlogBase):
    class Config():
           orm_mode = True


