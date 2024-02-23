import unittest
from filter_property_service import PropertyFilterService 
import mysql.connector

class TestPropertyFilterService(unittest.TestCase):
        
        #METHOD: do_get:
        def test_verify_jwt_token_invalid(self, mocker):

                mocker.patch.object(PropertyFilterService, 'verify_jwt_token', return_value=False)
                mock_request = mocker.Mock()
                mock_response = mocker.Mock()
                mock_wfile = mocker.Mock()
                mock_response.wfile = mock_wfile
                service = PropertyFilterService(mock_request, ('', 0), mock_response)
                service.do_GET()
                assert service.send_response.call_args[0][0] == 401
                assert service.send_header.call_args_list[0][0][0] == 'Content-type'
                assert service.send_header.call_args_list[0][0][1] == 'application/json'
                assert service.wfile.write.call_args[0][0] == b'Unauthorized'

        def test_exception_occurs(self, mocker):

                mocker.patch.object(PropertyFilterService, 'verify_jwt_token', side_effect=Exception('Invalid token'))
                mock_request = mocker.Mock()
                mock_response = mocker.Mock()
                mock_wfile = mocker.Mock()
                mock_response.wfile = mock_wfile
                service = PropertyFilterService(mock_request, ('', 0), mock_response)
                service.do_GET()
                assert service.send_response.call_args[0][0] == 500
                assert service.send_header.call_args_list[0][0][0] == 'Content-type'
                assert service.send_header.call_args_list[0][0][1] == 'application/json'
                assert service.wfile.write.call_args[0][0] == b'Internal Server Error'
                
        #METHOD: get_filtered_data
        def test_retrieves_filtered_data(self, mocker):

                mocker.patch('mysql.connector.connect')
                mocker.patch.object(PropertyFilterService, 'sanitize_string', return_value='mocked_value')
                service = PropertyFilterService()
                params_dict = {
                'param1': {'table': 'table1', 'value': 'value1'},
                'param2': {'table': 'table2', 'value': 'value2'}
                }
                query = 'SELECT * FROM properties WHERE table1.param1 = \'value1\' AND table2.param2 = \'value2\''
                data = [{'id': 1, 'name': 'property1'}, {'id': 2, 'name': 'property2'}]
                cursor_mock = mocker.Mock()
                cursor_mock.fetchall.return_value = data
                mocker.patch.object(mysql.connector, 'cursor', return_value=cursor_mock)
                execute_mock = mocker.Mock()
                mocker.patch.object(cursor_mock, 'execute', execute_mock)
                result = service.get_filtered_data(params_dict)
                execute_mock.assert_called_once_with(query)
                assert result == data

if __name__ == '__main__':
    unittest.main()
    
