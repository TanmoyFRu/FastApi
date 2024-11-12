from fastapi import APIRouter
from .. import models
from ..database import engine
from ..routers import blog, user

router = APIRouter(
    tags=["Login"]
)


@router.post('/login')
def login():
    return 'login'