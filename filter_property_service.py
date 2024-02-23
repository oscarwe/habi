import http.server
import json
import mysql.connector
from urllib.parse import urlparse, parse_qs 
import settings
from base import BaseRESTHandler

# Get database connection configuration from settings
DB_CONFIG = getattr(settings, 'DB_CONFIG', None)

class PropertyFilterService(BaseRESTHandler):
    """Service for filtering properties."""

    def do_GET(self):
        """Handle GET requests."""
        try:
            # Verify JWT token
            if not self.verify_jwt_token():
                self.send_response(401)
                self.end_headers()
                self.wfile.write(b'Unauthorized')
                return

            # Parse the URL to extract query parameters
            parsed_path = urlparse(self.path)
            self.query_params = parse_qs(parsed_path.query)
            
            # Get allowed parameters for this request from settings
            self.allowed_params = getattr(settings, 'ALLOWED_PARAMS_PROPERTY_FILTER', None)
            
            # Extract and compare allowed parameters using the parent class method
            extracted_params = self.extract_params()
            
            # Configure HTTP response
            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.end_headers()

            # Get filtered data from the database
            data = self.get_filtered_data(extracted_params)

            # Convert data to JSON and send as response
            self.wfile.write(json.dumps(data).encode())

        except Exception as e:
            # Proper error message handling involves avoiding exposure of sensitive information to end users.
            # It's essential to store these messages in logs for analysis by the development team.
            print(str(e))
            self.send_response(500)
            self.end_headers()
            self.wfile.write(b'Internal Server Error') 

    def get_filtered_data(self, params_dict=None):
        """Retrieve filtered data from the database."""
        try:
            # Establish connection to the database
            conn = mysql.connector.connect(**DB_CONFIG)
            cursor = conn.cursor(dictionary=True)

            # Build the base SQL query
            query = settings.FILTER_PROPERTY_QUERY

            # Add parameters to the query if available
            if params_dict:
                for key, value in params_dict.items():
                    table = self.sanitize_string(value['table'])
                    param_value = self.sanitize_string(value['value'])
                    key = self.sanitize_string(key)
                    query += f" AND {table}.{key} = '{param_value}'"

            # Execute the SQL query and get results
            cursor.execute(query)
            data = cursor.fetchall()

            # Close cursor and connection
            cursor.close()
            conn.close()

            return data
        except mysql.connector.Error as err:
            raise Exception("Error connecting to the database:", err)
        except Exception as e:
            print(str(e))
            raise Exception("An error occurred during execution")

# Run local server method for testing
def run_server(host='localhost', port=8000):
    """Run local HTTP server."""
    server_address = (host, port)
    httpd = http.server.HTTPServer(server_address, PropertyFilterService)
    print(f'Server is running at http://{host}:{port}')
    httpd.serve_forever()

if __name__ == '__main__':
    run_server()