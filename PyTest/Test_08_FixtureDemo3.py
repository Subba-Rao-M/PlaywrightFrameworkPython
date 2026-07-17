import pytest

"""
Fixtues in pytest are functions that setup test environment before test run
clean up after test execution
Fixtures are used to provide data, state or configuration to test functions

help in managing test dependencies and setup/teardown logic and 
provide reusable data across multiple test cases

Key Features:
1. Reusability: Fixtures can be reused across multiple test cases, reducing code duplication and improving maintainability.
2. Automatic Setup and Teardown: Fixtures can automatically set up the test environment before the test runs and clean up afterward, ensuring that tests are isolated and do not interfere with each other.
3. Scope - Control : Fixture can be run per test, per class, per module or per session
4. Dependency Injection: Pass fixture as argument for test function .Fixtures can be used to inject dependencies into test functions, allowing for more flexible and modular test design.

"""

@pytest.fixture()
def sample_data():
    print("SetUp - Creating test data")
    data = {"name": "John", "age": 30, "city": "New York"}
    return data
    yield
    print("TearDown - Cleaning up test data")

def test_example(sample_data):
    print("Test case is running with sample data")
    assert sample_data["name"] == "John"
    assert sample_data["age"] == 30
    assert sample_data["city"] == "New York"
    print("Test case executed successfully with sample data")