from rest_framework.viewsets import GenericViewSet
import os
from rest_framework.response import Response

import sqlalchemy as db
from sqlalchemy import func

from ..models import User, engine, Notes, Base

class Helper:

    def getNotesCreated(self, email):
        getNotes = db.select(User.notesCreated).filter_by(email=email)
        result = engine.connect().execute(getNotes)
        data = result.mappings().all()
        print(data)
        result.close()
        engine.dispose()
        return data[0]['notesCreated']

    def getMaxNotes(self):
        getMaxNotes = db.select(func.max(Notes.noteId))
        result = engine.connect().execute(getMaxNotes)
        data = result.mappings().all()
        print(data)
        result.close()
        engine.dispose()
        return data[0]['max_1']

    def getOldContent(self,noteId):
        getOldNoteContent = db.select(Notes.noteContent).filter_by(noteId=noteId)
        result = engine.connect().execute(getOldNoteContent)
        data = result.mappings().all()
        print(data)
        result.close()
        engine.dispose()
        return data[0]['notesCreated']

    def checkUserExists(self,email):
        checkUser = db.select(User).filter_by(email=email)
        result = engine.connect().execute(checkUser)
        data = result.mappings().all()
        print(data)
        result.close()
        engine.dispose()
        return len(data)

