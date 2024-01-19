from sqlalchemy import create_engine, MetaData
from sqlalchemy.orm import sessionmaker
from databases import Database
from sqlalchemy.pool import NullPool
from models import Base

DATABASE_URL = 'sqlite:///./data.db'

database = Database(DATABASE_URL)

engine = create_engine(DATABASE_URL, connect_args = {"check_same_thread": False}, poolclass=NullPool)

metadata = MetaData()

Base.metadata.create_all(bind=engine)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
