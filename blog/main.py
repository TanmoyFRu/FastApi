from fastapi import FastAPI
from . import schemas, models
# " . " means from the same directory

from .database import engine

app = FastAPI()


models.Base.metadata.create_all(bind = engine)


@app.post('/blog')
def create(request : schemas.Blog):
   return request