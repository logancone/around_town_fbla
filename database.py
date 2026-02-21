import sqlite3
from sqlalchemy import create_engine, Column, Integer, String, Date, Text
from sqlalchemy.orm import DeclarativeBase, sessionmaker, Mapped, mapped_column

from datetime import date

# Superclass for all table classes
class Base(DeclarativeBase):
    pass

# Create table for users
class User(Base):
    __tablename__ = 'users'

    id: Mapped[int] = mapped_column(primary_key=True)
    username: Mapped[str] = mapped_column(unique=True)
    password: Mapped[str]
    created_on: Mapped[date] = mapped_column(Date)

# Create table for businesses
class Business(Base):
    __tablename__ = 'businesses'

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str]
    owner_id: Mapped[int]
    category: Mapped[str]
    rating: Mapped[float] = mapped_column(nullable=True)
    thumbnail_link: Mapped[str]
    business_description: Mapped[str]

# Create table for reviews
class Review(Base):
    __tablename__ = 'reviews'
    
    id:Mapped[int] = mapped_column(primary_key=True)
    user_id: Mapped[int]
    business_id: Mapped[int]
    rating: Mapped[int]
    content: Mapped[str]
    timestamp: Mapped[date] = mapped_column(Date)

# Function to actually initialize all the tables
def create_tables():
    Base.metadata.create_all(engine)


# Creates the engine and the Session class, doesn't actually create a session though
engine = create_engine("sqlite:///sample_data.db")
# engine = create_engine("sqlite:///:memory:")
Session = sessionmaker(bind=engine)