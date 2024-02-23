import jwt
from jwt.exceptions import ExpiredSignatureError, InvalidTokenError
import re
import http.server
import settings

# Secret key for JWT
SECRET_KEY = getattr(settings, 'SECRET_KEY', None)

class BaseRESTHandler(http.server.BaseHTTPRequestHandler):
    """Base class for RESTful HTTP request handlers."""
    
    """https://docs.python.org/3.9/library/http.server.html"""
    """https://pyjwt.readthedocs.io/en/stable/"""

    def __init__(self, *args, **kwargs):
        """Initialize the base handler."""
        super().__init__(*args, **kwargs)
        self.allowed_params = None
        self.query_params = None
        
    def verify_jwt_token(self):
        """Verification of authentication token."""
        try:
            # Extract token from Authorization header
            auth_header = self.headers.get('Authorization')
            if not auth_header:
                return False

            auth_parts = auth_header.split(' ')
            if len(auth_parts) != 2:
                return False

            token = auth_parts[1]

            # Verify and decode JWT token
            jwt.decode(token, SECRET_KEY, algorithms=['HS256'])
            return True

        except ExpiredSignatureError:
            return False
        except InvalidTokenError:
            return False
        except Exception as e:
            print(str(e))
            return False
        
    def sanitize_string(self, string_data):
        """Format a string by encoding it to UTF-8 and removing strange characters."""
        try:
            # Remove non-ASCII characters and convert to UTF-8
            sanitized_string = str(string_data).encode('ascii', 'ignore').decode('utf-8', 'ignore')
            
            # Remove HTML tags
            sanitized_string = re.sub(r'<[^>]+>', '', sanitized_string)
            
            # Remove leading and trailing whitespaces
            sanitized_string = sanitized_string.strip()
            
            return sanitized_string
        except Exception as e:
            print(str(e))
            return ''
        
    def extract_params(self):
        """Extract allowed parameters and store them in a dictionary."""
        try:
            params = {}
            for key, value in self.query_params.items():
                if key in self.allowed_params:
                    table = self.allowed_params[key]
                    params[key] = {
                        'value': value[0],
                        'table': table
                    }
            return params
        except Exception as e:
            print(str(e))
            return None