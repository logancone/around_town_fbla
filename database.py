import sqlite3
from sqlalchemy import create_engine, Column, Integer, String, Date, Text, ForeignKey
from sqlalchemy.orm import DeclarativeBase, sessionmaker, Mapped, mapped_column

from datetime import date

from dataclasses import dataclass

import os

# Superclass for all table classes
class Base(DeclarativeBase):
    pass

# Create table for users
class User(Base):
    __tablename__ = 'users'

    id: Mapped[int] = mapped_column(primary_key=True)
    username: Mapped[str] = mapped_column(unique=True)
    password_hash: Mapped[str]
    lat: Mapped[float | None]
    lon: Mapped[float | None]
    created_on: Mapped[date] = mapped_column(Date)

# Create table for businesses
class Business(Base):
    __tablename__ = 'businesses'

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str]
    owner_id: Mapped[int]
    category: Mapped[str]
    avg_rating: Mapped[float] = mapped_column(default=0)
    rating_count: Mapped[int] = mapped_column(default=0)
    thumbnail_link: Mapped[str]
    business_description: Mapped[str]
    lat: Mapped[float]
    lon: Mapped[float]

# Create table for reviews
class Review(Base):
    __tablename__ = 'reviews'
    
    id:Mapped[int] = mapped_column(primary_key=True)
    user_id: Mapped[int]
    business_id: Mapped[int]
    rating: Mapped[int]
    content: Mapped[str]
    timestamp: Mapped[date] = mapped_column(Date)

# Create table for bookmarks
class Bookmark(Base):
    __tablename__ = 'bookmarks'

    user_id: Mapped[int] = mapped_column(ForeignKey(User.id), primary_key=True)
    business_id: Mapped[int] = mapped_column(ForeignKey(Business.id), primary_key=True)

# Create table to store each preset tag
class Tag(Base):
    __tablename__ = 'tags'

    id:Mapped[int] = mapped_column(primary_key=True)
    tag_name: Mapped[str] = mapped_column(unique=True)

# Create table to store each businesses' references to their tags
class BusinessTag(Base):
    __tablename__ = 'business_tags'

    business_id: Mapped[int] = mapped_column(ForeignKey(Business.id), primary_key=True)
    tag_id: Mapped[int] = mapped_column(ForeignKey(Tag.id), primary_key=True)

# Function to actually initialize all the tables
def create_tables():
    Base.metadata.create_all(engine)

# Creates the engine and the Session class, doesn't actually create a session though
engine = create_engine("sqlite:///app_database.db")

Session = sessionmaker(bind=engine)