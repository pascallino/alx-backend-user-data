#!/usr/bin/env python3
"""
Definition of Base class Auth
"""
from flask import request
from typing import List, TypeVar


class Auth:
    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """Check if authentication is required for the given path."""
        if path is None:
            return True
        elif excluded_paths is None or excluded_paths == []:
            return True
        elif path in excluded_paths:
            return False
        else:
            for i in excluded_paths:
                if i.startswith(path):
                    return False
                if path.startswith(i):
                    return False
                if i[-1] == "*":
                    if path.startswith(i[:-1]):
                        return False
        return True
        # Placeholder implementation, to be expanded later

    def authorization_header(self, request=None) -> str:
        """Extract the Authorization header from the request."""
        if request is None:
            return None
        header = request.headers.get('Authorization')
        if header is None:
            return None
        return header  # Placeholder implementation, to be expanded later

    def current_user(self, request=None) -> TypeVar('User'):
        """Retrieve the current user from the request."""
        return None  # Placeholder implementation, to be expanded later
