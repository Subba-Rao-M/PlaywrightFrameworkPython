#pip install pytest

# any pytest test case should start with test or test_ or end with _test

#define the method name with prefix test
#all preconditions can be marked as fixture
# if multiple test methods have same name, another test will override the first one instead of showing error

#Add the fixture to methods and pass the method name as argument in test method
#Scope = function - runs before each function
#Scope = module - runs once before execution of all methods, runs once for entire test file
#scope = class - fixture runs once for entire class, similar to module only but used with class standards

#scope = session - using conftest.py file, if fixture not present in current file, test will check in global file called conftest
#session executed only once per execution shared between multiple sessions

# To run multiple test cases files using terminal only and use pytest
#To do this all file names should start with Test
# To execute with print statement pytest -s
import pytest


@pytest.fixture(scope="function")
def precondition():
    print("Precondition added")

def testfirstcode(precondition):
    print("TC01_1 -First Test Executed")
    msg = "Hello"
    assert msg == "Hello"

def test_nextcode(precondition):
    print("TC01_2 - 1Next Test Executed")


def test_conftestcode(preworksetup):
    print("TC01_3 -Next Test Executed")


#Fixtures in pytest are functions used to setup and teardown the logics before and after code execution
# Helps in managing test dependencies, setup, teardown, share reusable data across multiple test cases
# key features of pytest fixtures
# 1) Reusability - > Define once and use multiple times
# 2) Automatic setup and teardown - > Handles pre-test and post test actions
# 3) Scope control - > Fixtures can be run per test, per class, per module or per session
# 4) Dependency injection - > Pass fixtures as test function arguments


##Best practices of framework design
#1) Avoid hard coding of test data
#Helps in generic code maintainability
#2) Externalize test data like from text, excel, csv , json files
#3) Implement Page object model to separate locators and actions from test file. This improves reusability readability and maintainability
#4) Centralize re-usable code. Like create utils file for common codes and configuration file conf.py. this avoids redundancy and provides consistency
#5) Define global environment variables - to run the code using parameters without changing code
# 6) Apply grouping using tags to run integrated tests
# 7) Generate html reports
# 8) Capture logs and screen shots
# 9) CI and CD integration with jenkins




# Run a specific test case in Firefox browser:
# ▶ pytest PlaywrightFramework/tests/TestCase_01_E2E_WebApiTesting.py --browser_name firefox

# Run all tests with custom base URL and browser:
# ▶ pytest --browser_name chrome --url_name https://staging.rahulshettyacademy.com

# Run all tests with tags like smoke or regression
# ▶ pytest -m smoke

# Run all tests with keywords used in test case name
# ▶ pytest -k Api

# Run only failed test cases
# ▶ pytest --last-failed

