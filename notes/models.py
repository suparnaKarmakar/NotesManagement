from django.db import models

# Create your models here.
import os
from colorama import Fore

from django.conf import settings
from sqlalchemy import create_engine, Column, String, Integer, Date, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.pool import NullPool

DEBUG = settings.DEBUG
Base = declarative_base()

db_username = 'root'
db_password = '1234'
db_host = 'localhost'
db_name = 'notes'

engine = create_engine(f'mysql://{db_username}:{db_password}@{db_host}/{db_name}', poolclass=NullPool, echo=True)

if DEBUG:
    pwd = '*' * (len(db_password)) if len(db_password) else "No Password"
    print(f"Username : {Fore.CYAN}{db_username}{Fore.RESET}\n Password : {Fore.CYAN}{db_password}{Fore.RESET}")


class User(Base):
    __tablename__ = 'user'
    email = Column('email',String, primary_key=True, nullable=False)
    password = Column('password', String, nullable=False)
    notesShared = Column('notesShared',String, nullable=True)
    notesCreated = Column('notesCreated', String, nullable=True)

    def __init__(self,email ,password, notesShared, notesCreated):
        self.email = email
        self.password = password
        self.notesShared = notesShared
        self.notesCreated = notesCreated


class Notes(Base):
    __tablename__ = 'notes'
    noteId = Column('noteId', Integer, primary_key=True, nullable=False)
    noteContent = Column('noteContent', String, nullable=False)
    noteCreatedBy = Column('noteCreatedBy', String, nullable=False)
    noteUpdatedBy = Column('noteUpdatedBy',String, nullable=True)
    noteSharedWith = Column('noteSharedWith', String, nullable=True)
    # updateHistory = Column('updateHistory', String, nullable=False)

    def __int__(self,noteId, noteContent, noteCreatedBy, noteUpdatedBy,noteSharedWith ):
        self.noteId = noteId
        self.noteContent = noteContent
        self.noteCreatedBy = noteCreatedBy
        self.noteUpdatedBy = noteUpdatedBy
        self.noteSharedWith = noteSharedWith
        # self.updateHistory = updateHistory
