from fastapi import FastAPI
from . import schemas
# " . " means from the same directory
from . import models
from .database import engine

app = FastAPI()


models.Base.metadata.create_all(engine)


@app.post('/blog')
def create(request : schemas.Blog):
   return request