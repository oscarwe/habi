from base import BaseRESTHandler
import unittest

class TestPropertyFilterService(unittest.TestCase):
    #METHOD: verify_jwt_token

    #Verify a valid JWT token and return True
    def test_valid_token_return_true(self):
            handler = BaseRESTHandler()
            token = "valid_token"
            auth_header = f"Bearer {token}"
            handler.headers = {'Authorization': auth_header}
            result = handler.verify_jwt_token()
            assert result == True
            
    #Return False if token is expired
    def test_expired_token_return_false(self):
            handler = BaseRESTHandler()
            token = "expired_token"
            auth_header = f"Bearer {token}"
            handler.headers = {'Authorization': auth_header}
            result = handler.verify_jwt_token()
            assert result == False
        
    #METHOD: sanitize_string

    #The method receives a string with only ASCII characters and no HTML tags. It returns the same string.
    def test_ascii_string_no_html_tags(self):

            handler = BaseRESTHandler()
            input_string = "This is a test string"
            expected_output = "This is a test string"
            output = handler.sanitize_string(input_string)
            assert output == expected_output

    #The method receives an empty string. It returns an empty string.
    def test_empty_string(self):

            handler = BaseRESTHandler()
            input_string = ""
            expected_output = ""
            output = handler.sanitize_string(input_string)
            assert output == expected_output
            
    #METHOD: extract_params

    #Extracts allowed parameters and stores them in a dictionary
    def test_extract_params_valid_keys(self):

            handler = BaseRESTHandler()
            handler.allowed_params = {'param1': 'table1', 'param2': 'table2'}
            handler.query_params = {'param1': ['value1'], 'param2': ['value2']}
            result = handler.extract_params()
            assert isinstance(result, dict)
            assert result == {'param1': {'value': 'value1', 'table': 'table1'}, 'param2': {'value': 'value2', 'table': 'table2'}}
            
    #Handles input data with invalid keys
    def test_extract_params_invalid_keys(self):

            handler = BaseRESTHandler()
            handler.allowed_params = {'param1': 'table1', 'param2': 'table2'}
            handler.query_params = {'param1': ['value1'], 'param3': ['value3']}
            result = handler.extract_params()
            assert result is None
            
if __name__ == '__main__':
    unittest.main()