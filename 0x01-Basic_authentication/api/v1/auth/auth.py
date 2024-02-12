from flask import request
from typing import List, TypeVar


class Auth:
    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """Check if authentication is required for the given path."""
        if path is None or excluded_paths is None or not excluded_paths:
            return True
        if excluded_paths == []:
            return True

        if not path.endswith('/'):
            path = path + '/'
        for excluded_path in excluded_paths:
            # Check if the path starts with an excluded path
            # heck if it starts with a / , add it and compare
            if not excluded_path.endswith('/'):
                excluded_path = excluded_path + '/'
            if path == excluded_path:
                return False

        return True   # Placeholder implementation, to be expanded later

    def authorization_header(self, request=None) -> str:
        """Extract the Authorization header from the request."""
        return None  # Placeholder implementation, to be expanded later

    def current_user(self, request=None) -> TypeVar('User'):
        """Retrieve the current user from the request."""
        return None  # Placeholder implementation, to be expanded later
