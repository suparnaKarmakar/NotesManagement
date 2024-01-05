import ast

from rest_framework.viewsets import GenericViewSet
import os
from rest_framework.response import Response

import sqlalchemy as db

from ..models import  engine, Notes, Base
import datetime

class updateNoteByIdRequestsListener(GenericViewSet):


    def updateNotesById(self, request):
        try:
            body = request.data
            noteId = body['noteId']
            updatedContent = body['updatedContent']
            noteUpdatedBy = body['noteUpdatedBy']
            # oldNoteContent = self.getOldContent(1)
            # test = self.makeUpdateHistory("abc", "xyz", "suparna@gmail.com")
            # print(test)


            updateNoteById = db.update(Base.metadata.tables[Notes.__tablename__]).filter_by(
                noteId=noteId).values(noteContent = updatedContent, noteUpdatedBy=noteUpdatedBy)
            with engine.connect() as conn:
                result = conn.execute(updateNoteById)
                conn.commit()
                print(result)
                conn.close()
                engine.dispose()


            return Response(data = f"Note {noteId} updated by {noteUpdatedBy}",
                            status = 200,
                            content_type = "application/json")
        except (Exception,BaseException) as err:
            return Response(data = str(err),
                            status=500,
                            content_type="application/json")



    # def updateHistory(self, oldContent, newContent, updatedBy):

    def getOldContent(self,noteId):
        getOldNoteContent = db.select(Notes.noteContent).filter_by(noteId=noteId)
        result = engine.connect().execute(getOldNoteContent)
        data = result.mappings().all()
        print(data)
        result.close()
        engine.dispose()
        return data[0]

    # def makeUpdateHistory(self, oldContent, newContent, email):
    #     if newContent != "" and oldContent is not None:
    #         # finalHistory = ast.literal_eval(oldContent)
    #         key = str(datetime.datetime.now()) + " - " + email
    #         finalHistory[key] = str(newContent)
    #         return str(finalHistory)
    #     elif newContent != "" and oldContent is None:
    #         finalHistory = {}
    #         key = str(datetime.datetime.now()) + " - " + email
    #         finalHistory[key] = str(newContent)
    #         return str(finalHistory)
    #     else :
    #         return oldContent

