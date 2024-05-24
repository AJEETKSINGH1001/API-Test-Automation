import unittest
import requests
import xmlrunner
import os

class TestReqresAPIPut(unittest.TestCase):
    BASE_URL = "https://reqres.in/api/users/2"

    def test_successful_put(self):
        """Test that the API returns a successful response for a valid PUT request."""
        payload = {
            "name": "morpheus",
            "job": "zion resident"
        }
        response = requests.put(self.BASE_URL, json=payload)
        self.assertEqual(response.status_code, 200, "Expected status code 200")
        json_data = response.json()
        self.assertIn("updatedAt", json_data, "Response JSON does not contain 'updatedAt'")

    def test_put_response_json_structure(self):
        """Test that the response JSON has the expected structure for a PUT request."""
        payload = {
            "name": "neo",
            "job": "the one"
        }
        response = requests.put(self.BASE_URL, json=payload)
        json_data = response.json()

        # Expected keys in the response
        expected_keys = ["name", "job", "updatedAt"]
        self.assertTrue(all(key in json_data for key in expected_keys),
                        "Response JSON does not have expected structure")

    def test_put_with_empty_payload(self):
        """Test the API's behavior with an empty payload."""
        response = requests.put(self.BASE_URL, json={})
        self.assertEqual(response.status_code, 200, "Expected status code 200 for empty payload")
        json_data = response.json()
        self.assertIn("updatedAt", json_data, "Response JSON does not contain 'updatedAt'")

    def test_put_with_invalid_payload(self):
        """Test the API's behavior with an invalid payload."""
        payload = {
            "invalid_field": "value"
        }
        response = requests.put(self.BASE_URL, json=payload)
        self.assertEqual(response.status_code, 200, "Expected status code 200 for invalid payload")
        json_data = response.json()
        self.assertIn("updatedAt", json_data, "Response JSON does not contain 'updatedAt'")

    def test_timeout_scenario(self):
        """Test the API's behavior under a timeout scenario."""
        payload = {
            "name": "trinity",
            "job": "hacker"
        }
        try:
            response = requests.put(self.BASE_URL, json=payload, timeout=0.001)
        except requests.exceptions.Timeout:
            self.assertTrue(True, "Expected timeout exception was raised")
        else:
            self.fail("Timeout exception was not raised")

    def test_long_strings_in_payload(self):
        """Test the API's response to very long strings in the name and job fields."""
        long_string = "a" * 1000
        payload = {
            "name": long_string,
            "job": long_string
        }
        response = requests.put(self.BASE_URL, json=payload)
        self.assertEqual(response.status_code, 200, "Expected status code 200")
        json_data = response.json()
        self.assertIn("updatedAt", json_data, "Response JSON does not contain 'updatedAt'")

    def test_put_with_missing_required_fields(self):
        """Test the API's behavior when required fields are missing from the payload."""
        payload = {
            "name": "missing job"
        }
        response = requests.put(self.BASE_URL, json=payload)
        self.assertEqual(response.status_code, 200, "Expected status code 200 for missing required fields")
        json_data = response.json()
        self.assertIn("updatedAt", json_data, "Response JSON does not contain 'updatedAt'")

    def test_put_with_additional_unspecified_fields(self):
        """Test the API's behavior with additional unspecified fields in the payload."""
        payload = {
            "name": "additional",
            "job": "fields",
            "extra_field": "extra_value"
        }
        response = requests.put(self.BASE_URL, json=payload)
        self.assertEqual(response.status_code, 200, "Expected status code 200")
        json_data = response.json()
        self.assertNotIn("extra_field", json_data, "Response JSON should not contain 'extra_field'")
        self.assertIn("updatedAt", json_data, "Response JSON does not contain 'updatedAt'")

    def test_large_payload(self):
        """Test the API's behavior with a very large payload size."""
        large_payload = {"name": "large", "job": "payload"}
        large_payload.update({f"key{i}": "value" for i in range(1000)})
        response = requests.put(self.BASE_URL, json=large_payload)
        self.assertEqual(response.status_code, 200, "Expected status code 200 for large payload")
        json_data = response.json()
        self.assertIn("updatedAt", json_data, "Response JSON does not contain 'updatedAt'")

    def test_special_characters_in_payload(self):
        """Test the API's handling of special characters in the name and job fields."""
        payload = {
            "name": "name!@#$%^&*()",
            "job": "job!@#$%^&*()"
        }
        response = requests.put(self.BASE_URL, json=payload)
        self.assertEqual(response.status_code, 200, "Expected status code 200 for special characters in payload")
        json_data = response.json()
        self.assertIn("updatedAt", json_data, "Response JSON does not contain 'updatedAt'")

    def test_numeric_values_in_fields(self):
        """Test the API's response when numeric values are provided in the name and job fields."""
        payload = {
            "name": 123,
            "job": 456
        }
        response = requests.put(self.BASE_URL, json=payload)
        self.assertEqual(response.status_code, 200, "Expected status code 200 for numeric values in fields")
        json_data = response.json()
        self.assertIn("updatedAt", json_data, "Response JSON does not contain 'updatedAt'")

    def test_null_values_in_fields(self):
        """Test the API's response when null values are provided in the name and job fields."""
        payload = {
            "name": None,
            "job": None
        }
        response = requests.put(self.BASE_URL, json=payload)
        self.assertEqual(response.status_code, 200, "Expected status code 200 for null values in fields")
        json_data = response.json()
        self.assertIn("updatedAt", json_data, "Response JSON does not contain 'updatedAt'")

    def test_boolean_values_in_fields(self):
        """Test the API's response when boolean values are provided in the name and job fields."""
        payload = {
            "name": True,
            "job": False
        }
        response = requests.put(self.BASE_URL, json=payload)
        self.assertEqual(response.status_code, 200, "Expected status code 200 for boolean values in fields")
        json_data = response.json()
        self.assertIn("updatedAt", json_data, "Response JSON does not contain 'updatedAt'")

    def test_array_in_fields(self):
        """Test the API's response when array values are provided in the name and job fields."""
        payload = {
            "name": ["name1", "name2"],
            "job": ["job1", "job2"]
        }
        response = requests.put(self.BASE_URL, json=payload)
        self.assertEqual(response.status_code, 200, "Expected status code 200 for array values in fields")
        json_data = response.json()
        self.assertIn("updatedAt", json_data, "Response JSON does not contain 'updatedAt'")

    def test_object_in_fields(self):
        """Test the API's response when object values are provided in the name and job fields."""
        payload = {
            "name": {"first": "John", "last": "Doe"},
            "job": {"title": "developer", "company": "company"}
        }
        response = requests.put(self.BASE_URL, json=payload)
        self.assertEqual(response.status_code, 200, "Expected status code 200 for object values in fields")
        json_data = response.json()
        self.assertIn("updatedAt", json_data, "Response JSON does not contain 'updatedAt'")

if __name__ == "__main__":
    # Ensure the output directory exists
    if not os.path.exists('test-reports'):
        os.makedirs('test-reports')

    # Run the tests and generate the XML report
    with open('test-reports/results.xml', 'wb') as output:
        unittest.main(testRunner=xmlrunner.XMLTestRunner(output=output), failfast=False, buffer=False, catchbreak=False)
