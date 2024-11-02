import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    email = Column(String(550), nullable=False)

    characters = relationship('Characters', back_populates='user')
    planets = relationship('Planets', back_populates='user')
    ships = relationship('Ships', back_populates='user')

class Characters(Base):
    __tablename__ = 'characters'
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    

    user_id = Column(Integer, ForeignKey('user.id'))
    user = relationship(User)

class Planets(Base):
    __tablename__ = 'planets'
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    

    user_id = Column(Integer, ForeignKey('user.id'))
    user = relationship(User)

class Ships(Base):
    __tablename__ = 'ships'
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    

    user_id = Column(Integer, ForeignKey('user.id'))

class Favorites(Base):
    __tablename__ = 'favorites'
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    

    characters_id = Column(Integer, ForeignKey('characters.id'))
    ships_id = Column(Integer, ForeignKey('ships.id'))
    planets_id = Column(Integer, ForeignKey('planets.id'))




## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')
