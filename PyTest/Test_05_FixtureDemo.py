import pytest

#yeild keywored is used to run steps after test case step execution

@pytest.fixture()
def setup():
    print("Fixture - Execute before test case step execution")
    yield
    print("Fixture - Execute steps after test case steps execution")

# pass the above fixture name as argument for below test
def test_fixtures(setup):
    print("I'm executing fixture method before this line")

def test_fixtureCT(preworksetup):
    print("Im running fixture from conftest for session")