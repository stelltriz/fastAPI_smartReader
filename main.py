from fastapi import FastAPI, HTTPException, Depends
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session
from database import *
from models import *
from typing import List

# Inicializar FastAPI

app = FastAPI()



app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"], # Allows all origins
    allow_credentials=True,
    allow_methods=["*"], # Allows all methods
    allow_headers=["*"], # Allows all header
)

# Função GET para Acessar todos os funcionários cadastrados

@app.get('/get_all_users', response_model=List[UserRead])
async def get_all_users(db: Session = Depends(get_db)):
    users = db.query(UserDB).all()
    return users 

# Função GET para acessar informações do funcionário de acordo com o ID

@app.get('/user/{edv}', response_model=UserRead)
async def get_user(edv: int, db: Session = Depends(get_db)):
    user = db.query(UserDB).filter(edv == UserDB.edv).first()
    if user is None:
        raise HTTPException(status_code=404, detail='User not found')
    return user

# Função PUT para editar/atualizar informações do funcionário

@app.put('/update_user/{id}', response_model=UserRead)
async def update_user(edv: int, upd_user: UserUpdate, db: Session = Depends(get_db)):
    
    db_user = db.query(UserDB).filter(UserDB.id == edv).first()

    if not db_user:
        raise HTTPException(status_code=404, detail='Item Not Found')

    for key, value in upd_user.dict().items():
        setattr(db_user, key, value)

    db.commit()
    db.refresh(db_user)
    return db_user

# Função POST para Adiconar/Criar informações de um funcionário 

@app.post('/user/', response_model=UserRead)
async def create_user(user: UserCreate, db: Session = Depends(get_db)):

    db_user = UserDB(**user.dict())
    db.add(db_user)

    db.commit()

    db.refresh(db_user)

    return db_user

# Função DELETE para deletar as informações de um funcionário

@app.delete('/delete_user/{id}')
async def delete_user(edv: int, db: Session = Depends(get_db)):
    db_user = db.query(UserDB).filter(UserDB.id == edv).first()
    
    if db_user:
        db.delete(db_user)
        db.commit()
        
        return {'message': f'User with id "{edv}" deleted', 'Deleted_user': db_user}
    else:
        raise HTTPException(status_code=404, detail='User Not Found')
