
from fastapi import FastAPI
from components.blog import blogmodel
from components.blog import blog
from components.database import engine
from components.login import authentication
from components.user import user
from components import Landing_page


app = FastAPI()

blogmodel.Base.metadata.create_all(bind=engine)


app.include_router(Landing_page.router)
app.include_router(authentication.router)
app.include_router(user.router)
app.include_router(blog.router)
