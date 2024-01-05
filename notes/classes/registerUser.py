from rest_framework.viewsets import GenericViewSet
import os
from rest_framework.response import Response

import sqlalchemy as db

from ..models import User, engine, Notes, Base
from .helperFunctions import Helper

class registerRequestsListener(GenericViewSet):




    def registerUser(self, request):
        try:
            body = request.data
            email = body['email']
            password = body['password']
            # check if user already exists
            userExists = Helper().checkUserExists(email)
            if userExists == 0:
                register = db.insert(Base.metadata.tables[User.__tablename__]).values(email = email, password = password)
                with engine.connect() as conn:
                    result = conn.execute(register)
                    conn.commit()
                    print(result)
                    conn.close()
                    engine.dispose()
                return Response(data = "Done",
                                status = 200,
                                content_type = "application/json")
            else:
                return Response(data=f"User with email {email} is already registered",
                                status=200,
                                content_type="application/json")
        except (Exception,BaseException) as err:
            return Response(data = str(err),
                            status=500,
                            content_type="application/json")