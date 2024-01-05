import ast

from rest_framework.viewsets import GenericViewSet
import os
from rest_framework.response import Response

import sqlalchemy as db
from sqlalchemy import text

from ..models import  engine, Notes, Base
import datetime

class searchNoteRequestsListener(GenericViewSet):


    def searchNote(self, request):
        try:
            body = request.data
            keywords = body['keywords']

            filter_conditions = " OR ".join([f"noteContent LIKE '%{keyword}%'" for keyword in keywords])
            query = db.select(Notes.noteId, Notes.noteContent).filter(text(filter_conditions))
            result = engine.connect().execute(query)
            data = result.mappings().all()
            print(data)
            result.close()
            engine.dispose()


            return Response(data = data,
                            status = 200,
                            content_type = "application/json")
        except (Exception,BaseException) as err:
            return Response(data = str(err),
                            status=500,
                            content_type="application/json")



