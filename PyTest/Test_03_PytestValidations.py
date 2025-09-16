import pytest


@pytest.fixture(scope="module")
def precondition():
    print("Precondition added")
    return "Pass"

@pytest.fixture(scope="function")
def secondwork():
    ##Add preconditions before method here like browser setup, driver setup
    print("SetUp required data")
    yield # Pause after function execution below statements gets called
    print("Add tear down details like closing browser, page, database connection")

def testfirstcode(precondition, secondwork): # return value from precondition catched here
    print("TC01_1 -First Test Executed")
    assert precondition == "Pass"

@pytest.mark.smoke
def testseconadcode(precondition, secondwork): # return value from precondition catched here
    print("TC01_2 -Second Test Executed")
    #Session scope didnot come into picture, to get session entire code needs to be executed from command prompt

@pytest.mark.skip
def testthirdcode(precondition, secondwork): # return value from precondition catched here
    print("TC01_1 -Third Test Executed")
#Run pytest from cmd
#run all test files -> pytest -s
#runSingle file - > pytest filename
#run single function from a test file - pytest filename::functionname

# To skip the file add mark above test case like pytest.mark.skip

# Tagging using pytest.mark.tagname
#Run using tag name - > pytest -m tagname like pytest -m smoke


