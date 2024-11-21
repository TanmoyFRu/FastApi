from passlib.context import CryptContext
import bcrypt



pwd_cxt = CryptContext(schemes = ['bcrypt'], deprecated = 'auto')

class Hash:
    @staticmethod
    def bcrypt(password : str) :
        return pwd_cxt.hash(password)
    
    @staticmethod
    def verify(hashed_password : str, plain_password : str):
        return pwd_cxt.verify(plain_password,hashed_password)
    
    