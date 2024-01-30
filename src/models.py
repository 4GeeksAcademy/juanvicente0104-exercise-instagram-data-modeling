import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er
from enum import Enum

Base = declarative_base()

class User(Base):
    __tablename__ = 'user'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    first_name = Column(String(100), nullable=False)
    last_name = Column(String(100), nullable=False)
    username = Column(String(30), nullable=False)
    email = Column(String(100), nullable=False)
    ###Pending relationships and foreign keys


class Follower(Base):
    __tablename__ = 'followers'
    id = Column(Integer, primary_key=True)
    user_from_id = Column(Integer,  ForeignKey('user.id'))
    user_to_id = Column(Integer,  ForeignKey('user.id'))

class Post(Base):
    __tablename__ = 'post'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer,  ForeignKey('user.id'))
    date = Column(String(50), nullable=False)
    caption = Column(String(300), nullable=False)
    likes = Column(Integer, nullable=False)
    comments = Column(Integer, nullable=False)

    comment = relationship("comment", backref="post")
    user = relationship("user", backref="post")
    media = relationship("media", backref="post")


class Comment(Base):
    __tablename__ = 'comment'   
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('user.id'))
    post_id = Column(Integer, ForeignKey('post.id'))
    date = Column(String(50), nullable=False)
    caption = Column(String(500), nullable=True)

class Media(Base):
    __tablename__ = 'media'  
    id = Column(Integer, primary_key=True)
    url = Column(String(50), nullable=False)
    post_id = Column(Integer, ForeignKey('post.id'))

## Draw from SQLAlchemy base
try:
    result = render_er(Base, 'diagram.png')
    print("Success! Check the diagram.png file")
except Exception as e:
    print("There was a problem genering the diagram")
    raise e
