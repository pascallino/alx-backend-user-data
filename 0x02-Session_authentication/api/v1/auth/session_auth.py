#!/usr/bin/env python3
"""
Definition of class SessionAuth
"""
import base64
from .auth import Auth
from typing import TypeVar

from models.user import User


class SessionAuth(Auth):
    """ Implement new session authentication mechanism:
    Authorization protocol methods
    """
    pass