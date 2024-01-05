import ast

from rest_framework.viewsets import GenericViewSet
import os
from rest_framework.response import Response

import sqlalchemy as db

from ..models import  engine, Notes, Base, User
import datetime
from .helperFunctions import Helper

class shareNoteByIdRequestsListener(GenericViewSet):


    def shareNotesById(self, request):
        try:
            body = request.data
            noteId = body['noteId']
            noteSharedWith = body['noteSharedWith']


            #check if the user with whom I am going to share the note exists or not

            userExist = Helper().checkUserExists(noteSharedWith)
            # print(userExist)
            if userExist == 1:

                # Prepare new list of people with whom notes was shared

                oldShares = self.getNotesSharedWithUser(noteId)
                newShares = ""
                if oldShares == None:
                    newShares = str(noteSharedWith)
                elif oldShares != None:
                    newShares = str(oldShares) + "," + str(noteSharedWith)
                print(newShares)

                ###############################################################################
                ############### UPDATE THE noteSharedWith COLUMN OF NOTES TABLE ###############
                ###############################################################################

                updateNotesSharedWith = db.update(Base.metadata.tables[Notes.__tablename__]).filter_by(
                    noteId=noteId).values(noteSharedWith=str(newShares))
                with engine.connect() as conn:
                    result = conn.execute(updateNotesSharedWith)
                    conn.commit()
                    print(result)
                    conn.close()
                    engine.dispose()

                # Prepare new list of noteIds for a given user

                oldNoteIds = self.getNotesShared(noteSharedWith)
                newNoteIds = ""
                if oldNoteIds == None:
                    newNoteIds = str(noteId)
                elif oldNoteIds != None:
                    newNoteIds = str(oldNoteIds) + "," + str(noteId)

                print(newNoteIds)

                ###############################################################################
                ############### UPDATE THE notesShared COLUMN OF USER TABLE ###############
                ###############################################################################

                updateUserNotesShared = db.update(Base.metadata.tables[User.__tablename__]).filter_by(
                    email=noteSharedWith).values(notesShared = newNoteIds)
                with engine.connect() as conn:
                    result = conn.execute(updateUserNotesShared)
                    conn.commit()
                    print(result)
                    conn.close()
                    engine.dispose()

                return Response(data = f"Note {noteId} shared with user {noteSharedWith}",
                                status = 200,
                                content_type = "application/json")
            else:
                return Response(data=f"User with email {noteSharedWith} does not exist",
                                status=200,
                                content_type="application/json")
        except (Exception,BaseException) as err:
            return Response(data = str(err),
                            status=500,
                            content_type="application/json")





    def getNotesSharedWithUser(self, noteId):
        getNotes = db.select(Notes).filter_by(noteId = noteId)
        result = engine.connect().execute(getNotes)
        data = result.mappings().all()
        print(data)
        result.close()
        engine.dispose()
        return data[0]['noteSharedWith']

    def getNotesShared(self,email):
        getNotes = db.select(User).filter_by(email=email)
        result = engine.connect().execute(getNotes)
        data = result.mappings().all()
        print(data)
        result.close()
        engine.dispose()
        return data[0]['notesShared']