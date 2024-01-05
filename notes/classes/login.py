from rest_framework.viewsets import GenericViewSet
import os
from rest_framework.response import Response

import sqlalchemy as db

from ..models import User, engine, Notes, Base
from .helperFunctions import Helper

class loginRequestsListener(GenericViewSet):

    def login(self, request):
        try:
            body = request.data
            email = body['email']
            password = body['password']
            # check if user already exists
            userExists = Helper().checkUserExists(email)
            if userExists == 1:

                return Response(data = f'User {email} logged',
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