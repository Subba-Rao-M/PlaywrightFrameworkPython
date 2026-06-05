import pytest

@pytest.mark.smoke
def test_firstProgram():
    msg = "Hello"
    assert msg == "Hi", "Assertion failed"

@pytest.mark.skip
def test_secondProgram():
    a= 4
    assert a != 0

@pytest.mark.xfail
def test_thirdProgram():
    print("Hello third test case")

"""
# Tagging using pytest.mark.tagname
#Run using tag name - > pytest -m tagname like pytest -m smoke

@pytest.mark.smoke

To skip the test 
@pytest.mark.skip

To skip the test case exectuion and but display in report 
@pytest.mark.xfail

"""