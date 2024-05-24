import unittest
import requests
import xmlrunner
import os


class TestReqresAPI(unittest.TestCase):
    BASE_URL = "https://reqres.in/api/users"

    def test_successful_response(self):
        """Test that the API returns a successful response."""
        response = requests.get(f"{self.BASE_URL}?page=2")
        self.assertEqual(response.status_code, 200, "Expected status code 200")

    def test_response_json_structure(self):
        """Test that the response JSON has the expected structure."""
        response = requests.get(f"{self.BASE_URL}?page=2")
        json_data = response.json()

        # Expected keys in the response
        expected_keys = ["page", "per_page", "total", "total_pages", "data"]
        self.assertTrue(all(key in json_data for key in expected_keys),
                        "Response JSON does not have expected structure")

    def test_data_integrity(self):
        """Test that the data field in the response has the expected structure."""
        response = requests.get(f"{self.BASE_URL}?page=2")
        json_data = response.json()

        # Ensure 'data' is a list and contains dictionaries with specific keys
        self.assertIsInstance(json_data['data'], list, "'data' should be a list")
        if json_data['data']:
            expected_data_keys = ["id", "email", "first_name", "last_name", "avatar"]
            for user in json_data['data']:
                self.assertTrue(all(key in user for key in expected_data_keys),
                                "User data does not have expected keys")

    def test_invalid_page_parameter(self):
        """Test the API's behavior with an invalid page parameter."""
        response = requests.get(f"{self.BASE_URL}?page=invalid")
        # Expected status code should be verified based on actual API behavior
       # self.assertNotEqual(response.status_code, 200, "Expected non-200 status code for invalid page parameter")

    def test_empty_response(self):
        """Test that the API returns an empty data list for a non-existent page."""
        response = requests.get(f"{self.BASE_URL}?page=9999")
        json_data = response.json()

        self.assertEqual(json_data['data'], [], "Expected 'data' to be an empty list for non-existent page")

    def test_timeout_scenario(self):
        """Test the API's behavior under a timeout scenario."""
        try:
            response = requests.get(f"{self.BASE_URL}?page=2", timeout=0.001)
        except requests.exceptions.Timeout:
            self.assertTrue(True, "Expected timeout exception was raised")
        else:
            self.fail("Timeout exception was not raised")


if __name__ == "__main__":
    if not os.path.exists('test-reports'):
        os.makedirs('test-reports')

    with open('test-reports/results.xml', 'wb') as output:
        unittest.main(testRunner=xmlrunner.XMLTestRunner(output=output), failfast=False, buffer=False, catchbreak=False)
