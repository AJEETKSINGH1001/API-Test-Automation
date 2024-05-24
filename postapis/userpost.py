import unittest
import requests
import xmlrunner
import os

class TestReqresAPIPost(unittest.TestCase):
    BASE_URL = "https://reqres.in/api/users"

    def test_successful_post(self):
        """Test that the API returns a successful response for a valid POST request."""
        payload = {
            "name": "morpheus",
            "job": "leader"
        }
        response = requests.post(self.BASE_URL, json=payload)
        self.assertEqual(response.status_code, 201, "Expected status code 201")
        json_data = response.json()
        self.assertIn("id", json_data, "Response JSON does not contain 'id'")
        self.assertIn("createdAt", json_data, "Response JSON does not contain 'createdAt'")

    def test_post_response_json_structure(self):
        """Test that the response JSON has the expected structure for a POST request."""
        payload = {
            "name": "neo",
            "job": "the one"
        }
        response = requests.post(self.BASE_URL, json=payload)
        json_data = response.json()

        # Expected keys in the response
        expected_keys = ["name", "job", "id", "createdAt"]
        self.assertTrue(all(key in json_data for key in expected_keys),
                        "Response JSON does not have expected structure")

    def test_post_with_empty_payload(self):
        """Test the API's behavior with an empty payload."""
        response = requests.post(self.BASE_URL, json={})
        self.assertEqual(response.status_code, 400, "Expected status code 400 for empty payload")

    def test_post_with_invalid_payload(self):
        """Test the API's behavior with an invalid payload."""
        payload = {
            "invalid_field": "value"
        }
        response = requests.post(self.BASE_URL, json=payload)
        self.assertEqual(response.status_code, 400, "Expected status code 400 for invalid payload")

    def test_timeout_scenario(self):
        """Test the API's behavior under a timeout scenario."""
        payload = {
            "name": "trinity",
            "job": "hacker"
        }
        try:
            response = requests.post(self.BASE_URL, json=payload, timeout=0.001)
        except requests.exceptions.Timeout:
            self.assertTrue(True, "Expected timeout exception was raised")
        else:
            self.fail("Timeout exception was not raised")

    def test_duplicate_user_creation(self):
        """Test the API's response to creating a user with the same details more than once."""
        payload = {
            "name": "morpheus",
            "job": "leader"
        }
        response1 = requests.post(self.BASE_URL, json=payload)
        response2 = requests.post(self.BASE_URL, json=payload)
        self.assertEqual(response1.status_code, 201, "Expected status code 201 for the first request")
        self.assertEqual(response2.status_code, 201, "Expected status code 201 for the second request")
        self.assertNotEqual(response1.json()["id"], response2.json()["id"], "Expected different IDs for each creation")

    def test_long_strings_in_payload(self):
        """Test the API's response to very long strings in the name and job fields."""
        long_string = "a" * 1000
        payload = {
            "name": long_string,
            "job": long_string
        }
        response = requests.post(self.BASE_URL, json=payload)
        self.assertEqual(response.status_code, 201, "Expected status code 201")
        json_data = response.json()
        self.assertIn("id", json_data, "Response JSON does not contain 'id'")
        self.assertIn("createdAt", json_data, "Response JSON does not contain 'createdAt'")

    def test_post_with_missing_required_fields(self):
        """Test the API's behavior when required fields are missing from the payload."""
        payload = {
            "name": "missing job"
        }
        response = requests.post(self.BASE_URL, json=payload)
        self.assertEqual(response.status_code, 400, "Expected status code 400 for missing required fields")

    def test_post_with_additional_unspecified_fields(self):
        """Test the API's behavior with additional unspecified fields in the payload."""
        payload = {
            "name": "additional",
            "job": "fields",
            "extra_field": "extra_value"
        }
        response = requests.post(self.BASE_URL, json=payload)
        self.assertEqual(response.status_code, 201, "Expected status code 201")
        json_data = response.json()
       # self.assertNotIn("extra_field", json_data, "Response JSON should not contain 'extra_field'")
        self.assertIn("id", json_data, "Response JSON does not contain 'id'")
        self.assertIn("createdAt", json_data, "Response JSON does not contain 'createdAt'")

if __name__ == "__main__":
    # Ensure the output directory exists
    if not os.path.exists('test-reports'):
        os.makedirs('test-reports')

    # Run the tests and generate the XML report
    with open('test-reports/results.xml', 'wb') as output:
        unittest.main(testRunner=xmlrunner.XMLTestRunner(output=output), failfast=False, buffer=False, catchbreak=False)
