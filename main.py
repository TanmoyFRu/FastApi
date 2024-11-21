
from fastapi import FastAPI
from components.blog import blogModel
from components.blog import blogRoutes
from components.database import engine
from components.login import authenticationRoutes
from components.user import userRoutes
from components import Landing_page


app = FastAPI()

blogModel.Base.metadata.create_all(bind=engine)


app.include_router(Landing_page.router)
app.include_router(authenticationRoutes.router)
app.include_router(userRoutes.router)
app.include_router(blogRoutes.router)
