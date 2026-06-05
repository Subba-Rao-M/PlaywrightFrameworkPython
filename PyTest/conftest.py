#conftest.py file is used to define fixtures and hooks that are shared with multiple python files
# fixtures will incude setup or teardown information
#conftest file will have access to all test files available in folder like centralized file
# first test will check current file and if not available check in conftest file for fixtures

#scope = session - using conftest.py file, if fixture not present in current file, test will check in global file called conftest
#session executed only once per execution shared between multiple sessions

import pytest
@pytest.fixture(scope="session")
def preworksetup():
    print("This is from conftest initialization of precondition")


@pytest.fixture(scope= "class")
def setup():
    print("Fixture - Execute before test case step execution")
    yield
    print("Fixture - Execute steps after test case steps execution")

@pytest.fixture()
def dataLoad():
    print("This is data load fixture to send data at run time")
    return ["Subb", "Rao", "rahulshettyacademy.com"]

#request is instance of fixture and which is tied to return param values
@pytest.fixture(params=[("chrome", "Subba"), ("edge", "rao"), "firefox"])
def crossBrowser(request):
    return request.param