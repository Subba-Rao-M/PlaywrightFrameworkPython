"""
to install pip install pytest-html
to open html report pytest --html=report.html

to install paraller execution package
pip install pytest-xdist

to run parallel
pytest -n auto

"""

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