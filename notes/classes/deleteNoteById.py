import ast

from rest_framework.viewsets import GenericViewSet
import os
from rest_framework.response import Response

import sqlalchemy as db

from ..models import  engine, Notes, Base
import datetime

class deleteNoteByIdRequestsListener(GenericViewSet):


    def deleteNoteById(self, request):
        try:
            body = request.data
            noteId = body['noteId']

            # noteUpdatedBy = body['noteUpdatedBy']



            # updateNoteById = db.update(Base.metadata.tables[Notes.__tablename__]).filter_by(
            #     noteId=noteId).values(noteContent = updatedContent, noteUpdatedBy=noteUpdatedBy)
            deleteNote = db.delete(Notes).filter_by(noteId = noteId)
            with engine.connect() as conn:
                result = conn.execute(deleteNote)
                conn.commit()
                print(result)
                conn.close()
                engine.dispose()


            return Response(data = f"Note with id {noteId} deleted.",
                            status = 200,
                            content_type = "application/json")
        except (Exception,BaseException) as err:
            return Response(data = str(err),
                            status=500,
                            content_type="application/json")





