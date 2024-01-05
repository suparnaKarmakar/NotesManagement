from rest_framework.viewsets import GenericViewSet
import os
from rest_framework.response import Response

import sqlalchemy as db

from ..models import User, engine, Notes, Base
from .helperFunctions import Helper


class createNoteRequestsListener(GenericViewSet):

    def createNote(self, request):
        try:
            body = request.data
            noteContent = body['noteContent']
            noteCreatedBy = request.headers.get('noteCreatedBy')

            print(noteContent, noteCreatedBy)
            stat = db.insert(Base.metadata.tables[Notes.__tablename__]).values( noteContent = noteContent, noteCreatedBy = noteCreatedBy)

            with engine.connect() as conn:
                result = conn.execute(stat)
                conn.commit()
                print(result)
                conn.close()
                engine.dispose()

            noteId = Helper().getMaxNotes()
            print(noteId)

            oldcreates = Helper().getNotesCreated(noteCreatedBy)
            print(oldcreates)
            newcreates = ""
            if oldcreates == None:
                newcreates = str(noteId)
            elif oldcreates != None:
                newcreates = str(oldcreates) + "," + str(noteId)

            updateUsersCreations = db.update(Base.metadata.tables[User.__tablename__]).filter_by(email = noteCreatedBy).values(notesCreated = newcreates )
            with engine.connect() as conn:
                result = conn.execute(updateUsersCreations)
                conn.commit()
                print(result)
                conn.close()
                engine.dispose()

            return Response(data = f"Note {noteId} created by {noteCreatedBy}",
                            status = 200,
                            content_type = "application/json")
        except (Exception,BaseException) as err:
            return Response(data = str(err),
                            status=500,
                            content_type="application/json")