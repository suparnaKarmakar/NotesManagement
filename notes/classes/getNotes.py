from rest_framework.viewsets import GenericViewSet
import os
from rest_framework.response import Response

import sqlalchemy as db

from ..models import  engine, Notes
from rest_framework.throttling import UserRateThrottle

class getNotesRequestsListener(GenericViewSet):
    throttle_classes = [UserRateThrottle]

    def getNotes(self, request):
        try:
            stat = db.select(Notes)
            result = engine.connect().execute(stat)
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