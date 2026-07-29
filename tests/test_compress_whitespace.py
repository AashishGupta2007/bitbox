import pytest
from tools.compress_whitespace import run


def test_compress_whitespace_basic():
    assert run("hello   world") == "hello world"
    assert run("  hello   world  ") == " hello world "
    assert run("a\t\tb\n\nc") == "a b c"


def test_compress_whitespace_single_space():
    assert run("hello world") == "hello world"


def test_compress_whitespace_no_spaces():
    assert run("helloworld") == "helloworld"


def test_compress_whitespace_empty():
    assert run("") == ""


def test_compress_whitespace_no_args():
    assert run() == "Error: expected a string argument"
