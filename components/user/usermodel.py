from sqlalchemy import Column,Integer,String, ForeignKey
from ..database import Base
from sqlalchemy.orm import relationship




class User(Base):
    __tablename__ = 'users_post'
    
    id = Column(Integer, primary_key = True,index=True)
    name = Column(String)
    email = Column(String)
    password = Column(String)
    
    blogs = relationship('Blog', back_populates='creator')