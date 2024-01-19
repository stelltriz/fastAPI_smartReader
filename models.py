from pydantic import BaseModel, validator
from sqlalchemy import Column, Integer, String, Float
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()


class UserCreate(BaseModel):
    edv: int 
    name: str
    sobrenome: str
    area: str

    @validator('edv')
    def validarCode(cls, value):
        if len(str(value)) != 8:
            raise ValueError('Código Inválido!')
        return value
    

class UserRead(BaseModel):
    id: int
    edv: int
    name: str
    sobrenome: str
    area: str
   

class UserUpdate(BaseModel):
    edv: int
    name: str
    sobrenome: str
    area: str
    
    @validator('edv')
    def validarEdv(cls, value):
        if len(str(value)) != 8:
            raise ValueError('EDV Inválido!')
        return value
    

class UserDB(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key = True, index=True)
    edv = Column(Integer, primary_key = True, index=True)
    name = Column(String, index=True)
    sobrenome = Column(String, index=True)
    area = Column(String, index=True)