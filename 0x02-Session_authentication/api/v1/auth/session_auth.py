#!/usr/bin/env python3
"""
Definition of class SessionAuth
"""
import base64
from .auth import Auth
from typing import TypeVar
from uuid import uuid4

from models.user import User


class SessionAuth(Auth):
    """ Implement new session authentication mechanism:
    Authorization protocol methods
    """
    user_id_by_session_id = {}

    def create_session(self, user_id: str = None) -> str:
        """ Create the session using uuid4
        where key is the uuid and value is the user_id"""
        # Return None if user_id is None or not a string
        if user_id is None or not isinstance(user_id, str):
            return None

        # Generate Session ID using uuid4()
        session_id = str(uuid4())

        # Store the Session ID and user_id in the class attribute dictionary
        self.user_id_by_session_id[session_id] = user_id

        # Return the Session ID
        return session_id

    def user_id_for_session_id(self, session_id: str = None) -> str:
        """ Return None if session_id is None or not a string """
        if session_id is None or not isinstance(session_id, str):
            return None

        # Retrieve the User ID based on the Session ID using .get() method
        user_id = self.user_id_by_session_id.get(session_id)

        # Return the User ID
        return user_id

    def current_user(self, request=None):
        """
        Return a user instance based on a cookie value
        Args:
            request : request object containing cookie
        Return:
            User instance
        """
        session_cookie = self.session_cookie(request)
        user_id = self.user_id_for_session_id(session_cookie)
        user = User.get(user_id)
        return user

    def destroy_session(self, request=None):
        """
        Deletes a user session
        """
        if request is None:
            return False
        session_cookie = self.session_cookie(request)
        if session_cookie is None:
            return False
        user_id = self.user_id_for_session_id(session_cookie)
        if user_id is None:
            return False
        del self.user_id_by_session_id[session_cookie]
        return True
