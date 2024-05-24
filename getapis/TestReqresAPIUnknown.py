import unittest
import requests
import xmlrunner
import os

class TestReqresAPIUnknown(unittest.TestCase):
    BASE_URL = "https://reqres.in/api/unknown"

    def test_successful_response(self):
        """Test that the API returns a successful response."""
        response = requests.get(f"{self.BASE_URL}/2")
        self.assertEqual(response.status_code, 200, "Expected status code 200")

    def test_response_json_structure(self):
        """Test that the response JSON has the expected structure."""
        response = requests.get(f"{self.BASE_URL}/2")
        json_data = response.json()

        # Expected keys in the response
        expected_keys = ["data", "support"]
        self.assertTrue(all(key in json_data for key in expected_keys),
                        "Response JSON does not have expected structure")

    def test_data_integrity(self):
        """Test that the data field in the response has the expected structure."""
        response = requests.get(f"{self.BASE_URL}/2")
        json_data = response.json()

        # Ensure 'data' contains a dictionary with specific keys
        expected_data_keys = ["id", "name", "year", "color", "pantone_value"]
        self.assertIsInstance(json_data['data'], dict, "'data' should be a dictionary")
        self.assertTrue(all(key in json_data['data'] for key in expected_data_keys),
                        "Data does not have expected keys")

    def test_invalid_resource(self):
        """Test the API's behavior with an invalid resource ID."""
        response = requests.get(f"{self.BASE_URL}/9999")
        self.assertEqual(response.status_code, 404, "Expected status code 404 for non-existent resource")

    def test_timeout_scenario(self):
        """Test the API's behavior under a timeout scenario."""
        try:
            response = requests.get(f"{self.BASE_URL}/2", timeout=0.001)
        except requests.exceptions.Timeout:
            self.assertTrue(True, "Expected timeout exception was raised")
        else:
            self.fail("Timeout exception was not raised")

if __name__ == "__main__":
    # Ensure the output directory exists
    if not os.path.exists('test-reports'):
        os.makedirs('test-reports')

    # Run the tests and generate the XML report
    with open('test-reports/results.xml', 'wb') as output:
        unittest.main(testRunner=xmlrunner.XMLTestRunner(output=output), failfast=False, buffer=False, catchbreak=False)
