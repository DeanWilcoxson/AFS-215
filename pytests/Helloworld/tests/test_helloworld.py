import pytest
from lib.helloworld import Hello
# class test_helloworld:
# def test_helloworld(self):
def test_helloworld():
    hello = Hello("Dean")
    assert hello == "Hello world my name is Dean"