import pytest
from tools.is_happy_number import run

def test_is_happy_number_positive():
    assert run("19") == "True"
    assert run("7") == "True"
    assert run("1") == "True"

def test_is_happy_number_unhappy():
    assert run("4") == "False"
    assert run("2") == "False"

def test_is_happy_number_invalid_or_negative():
    assert run("0") == "False"
    assert run("-19") == "False"
    assert run("abc") == "Error: argument must be an integer"
    assert run() == "Error: expected an integer"
