import pytest

# if fixture scope is class it will be executed once before class

@pytest.mark.usefixtures("setup")
class TestFixtureDemo:

    def test_fixtures(self):
        print("I'm executing fixture method before this line")

    def test_fixtureCT(self):
        print("Im running fixture from conftest for session")

    def test_fixtureDemo1(self):
        print("Class level fixture execution")