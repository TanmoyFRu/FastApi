from sqlalchemy import Column,Integer,String, ForeignKey
from ..database import Base
from sqlalchemy.orm import relationship
from ..user.usermodel import User


class Blog(Base):
    __tablename__ = 'blogs_post'
    
    id = Column(Integer, primary_key=True,index=True)
    title = Column(String)
    body = Column(String)
    user_id = Column(Integer, ForeignKey( "users_post.id"))
    
    User.creator = relationship("User", back_populates='blogs')
    

     