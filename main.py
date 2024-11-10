from fastapi import FastAPI
from typing import Optional
from pydantic import BaseModel
import uvicorn
# creating an Instance --> app
app = FastAPI()


@app.get('/blog')
# only GET 10 published blogs
# path operation decorator --> @app
# operation --> GET
# path --> ("/")
def index(limit = 10,published : bool = True, sort: Optional[str] = None):
# path operation function --> def index()
 if published:
    return {'data': f'{limit} published blog from the db'}
 else:
    return {'data': f'{limit} blog from the db'}

    
@app.get('/blog/unpublished')
def unpublished(): 
    return {'data': "all Unpublished Blogs"}
    
@app.get('/blog/{id}')
# path operation decorator --> @app
# operation --> GET
# path --> ("/about")
# {id} --> path parameter
def show(id : int):
    #path operation function --> def show()
    #fetch blog id = id
    return {'data': id}


@app.get('/blog/{id}/comments')
def comments(id : int): 
    return {'data':{'comments':{'1','2'}}}

class Blog(BaseModel):
    title : str
    body : str
    published: Optional[bool]

@app.post('/blog')
def create_blog(request : Blog):
    return {'data':f'blog is created with the Title as {request.title}'}

# if __name__ == '__main__':
#     uvicorn.run(app,host = '127.0.0.1',port=9000)