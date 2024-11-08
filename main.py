from fastapi import FastAPI

# creating an Instance --> app
app = FastAPI()


@app.get('/blog')
# only GET 10 published blogs
# path operation decorator --> @app
# operation --> GET
# path --> ("/")
def index(limit,published : bool):
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
def comments(id): 
    return {'data':{'comments':{'1','2'}}}
    