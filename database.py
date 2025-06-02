from sqlalchemy import create_engine, Column, Integer, String, Text, ForeignKey, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship
from datetime import datetime
from config import POSTGRES_URI

Base = declarative_base()
engine = create_engine(POSTGRES_URI)
SessionLocal = sessionmaker(bind=engine)

class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, default="Guest User")
    created_at = Column(DateTime, default=datetime.utcnow)

class DateSession(Base):
    __tablename__ = "dates"
    id = Column(Integer, primary_key=True, index=True)
    timestamp = Column(DateTime, default=datetime.utcnow)

class Prompt(Base):
    __tablename__ = "prompts"
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    date_id = Column(Integer, ForeignKey("dates.id"))
    text = Column(Text)
    user = relationship("User")
    date = relationship("DateSession")

class Response(Base):
    __tablename__ = "responses"
    id = Column(Integer, primary_key=True, index=True)
    prompt_id = Column(Integer, ForeignKey("prompts.id"))
    text = Column(Text)
    prompt = relationship("Prompt")

def init_db():
    Base.metadata.create_all(bind=engine)