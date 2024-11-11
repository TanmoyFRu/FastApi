from pydantic import BaseModel



class Blog(BaseModel):
    title:str
    body:str
    
    
class Show_Blog(Blog):
    class Config():
        orm_mode = True