#conftest.py file is used to define fixtures and hooks that are shared with multiple python files
#conftest file will have access to all test files available in folder like centralized file
# first test will check current file and if not available check in conftest file for fixtures

#scope = session - using conftest.py file, if fixture not present in current file, test will check in global file called conftest
#session executed only once per execution shared between multiple sessions

import pytest
@pytest.fixture(scope="session")
def preworksetup():
    print("This is from conftest initialization of precondition")