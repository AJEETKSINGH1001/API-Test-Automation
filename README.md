Repository Description:

Title: API Test Automation Suite for Reqres.in APIs

Description:

This Git repository contains a comprehensive test automation suite for testing various APIs provided by Reqres.in, a popular online REST API testing service. The suite includes Python scripts for conducting unit tests on both GET and POST endpoints offered by Reqres.in.

Features:

GET API Tests: Includes test cases for validating the GET endpoints:

https://reqres.in/api/users?page=2
https://reqres.in/api/unknown/2
POST API Test: Covers test scenarios for the POST endpoint:

https://reqres.in/api/users
Scenario Coverage: Each test script covers a wide range of scenarios, including:

Successful requests
Response validation
Error handling
Timeout scenarios
Duplicate user creation
Handling long strings in payload
Missing required fields
Additional unspecified fields
Structured Approach: The test scripts are structured following industry best practices and maintainability principles. Each script contains test methods within a dedicated test case class, utilizing the unittest framework.

Reporting: Test reports are automatically generated in XML format and stored in the test-reports/ directory. Optionally, XML reports can be converted to HTML format for enhanced readability.

Ease of Use: The repository provides a straightforward setup, allowing users to clone the repository and execute the tests locally on their development environment.

Contribution: Contributions and enhancements to the test suite are welcome. Users can fork the repository, make modifications, and submit pull requests to contribute to the project's improvement.

Usage Instructions:

Clone the repository to your local environment.
Ensure Python and required libraries (such as requests and unittest-xml-reporting) are installed.
Run the test scripts using Python to validate the behavior of Reqres.in APIs under various scenarios.
Optionally, convert XML test reports to HTML format for better readability using tools like junit2html.
Note: Ensure proper documentation and code comments are maintained for better understanding and collaboration among contributors.
