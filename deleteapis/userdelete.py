import unittest
import requests
import xmlrunner
import os

class TestReqresAPIDelete(unittest.TestCase):
    BASE_URL = "https://reqres.in/api/users/2"

    def test_successful_delete(self):
        """Test that the API returns a successful response for a valid DELETE request."""
        response = requests.delete(self.BASE_URL)
        self.assertEqual(response.status_code, 204, "Expected status code 204 for successful DELETE request")

    def test_delete_non_existent_user(self):
        """Test the API's response when attempting to delete a non-existent user."""
        response = requests.delete("https://reqres.in/api/users/9999")
        self.assertEqual(response.status_code, 204, "Expected status code 204 for non-existent user")

    def test_delete_with_invalid_endpoint(self):
        """Test the API's response when using an invalid endpoint."""
        response = requests.delete("https://reqres.in/api/userz/2")
        self.assertEqual(response.status_code, 404, "Expected status code 404 for invalid endpoint")

    def test_delete_with_invalid_method(self):
        """Test the API's response when using an invalid HTTP method."""
        response = requests.post(self.BASE_URL)
        self.assertEqual(response.status_code, 405, "Expected status code 405 for invalid HTTP method")

    def test_timeout_scenario(self):
        """Test the API's behavior under a timeout scenario."""
        try:
            response = requests.delete(self.BASE_URL, timeout=0.001)
        except requests.exceptions.Timeout:
            self.assertTrue(True, "Expected timeout exception was raised")
        else:
            self.fail("Timeout exception was not raised")

    def test_delete_with_query_parameters(self):
        """Test the API's response when adding query parameters to the DELETE request."""
        response = requests.delete(f"{self.BASE_URL}?param=value")
        self.assertEqual(response.status_code, 204, "Expected status code 204 even with query parameters")

    def test_delete_with_headers(self):
        """Test the API's response when adding custom headers to the DELETE request."""
        headers = {
            "Custom-Header": "value"
        }
        response = requests.delete(self.BASE_URL, headers=headers)
        self.assertEqual(response.status_code, 204, "Expected status code 204 even with custom headers")

    def test_delete_with_body(self):
        """Test the API's response when adding a body to the DELETE request (though unusual)."""
        body = {
            "name": "morpheus"
        }
        response = requests.delete(self.BASE_URL, json=body)
        self.assertEqual(response.status_code, 204, "Expected status code 204 even with body in request")

    def test_delete_with_authentication(self):
        """Test the API's response when adding authentication (though not required)."""
        auth = ("user", "pass")
        response = requests.delete(self.BASE_URL, auth=auth)
        self.assertEqual(response.status_code, 204, "Expected status code 204 even with authentication")

    def test_delete_with_invalid_authentication(self):
        """Test the API's response with invalid authentication details."""
        auth = ("invalid_user", "invalid_pass")
        response = requests.delete(self.BASE_URL, auth=auth)
        self.assertEqual(response.status_code, 204, "Expected status code 204 for invalid authentication")

if __name__ == "__main__":
    # Ensure the output directory exists
    if not os.path.exists('test-reports'):
        os.makedirs('test-reports')

    # Run the tests and generate the XML report
    with open('test-reports/results.xml', 'wb') as output:
        unittest.main(testRunner=xmlrunner.XMLTestRunner(output=output), failfast=False, buffer=False, catchbreak=False)
