import pytest

@pytest.mark.usefixtures("dataLoad", "crossBrowser")
class TestDataLoadExample:

    def test_userProfile(self, dataLoad):
        print("Dataload test")
        print(dataLoad[0])
        print(dataLoad[1])


    def test_crossBrowser(self, crossBrowser):
        print("Cross Browser testing")
        print(crossBrowser) # fetch all values
        print(crossBrowser[0]) #Parameterized data and fetch only first set of values