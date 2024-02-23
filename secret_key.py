# This file was used to generate a secret key for authentication for the web service.

import secrets
import jwt
import datetime

# Generate a random secret key for authentication
SECRET_KEY = secrets.token_urlsafe(32)

# Print the generated secret key
print(SECRET_KEY)

# Define the payload of the token (data to include in the token)
payload = {
    'user_id': 123456,
    'username': 'example_user',
    'exp': datetime.datetime.utcnow() + datetime.timedelta(hours=1)  # Expires in 1 hour
}

# Generate the JWT token
token = jwt.encode(payload, SECRET_KEY, algorithm='HS256')

# Print the token for the HTTP request header authorization
print(token)