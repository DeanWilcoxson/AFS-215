import pytest
from lib.Fizzbuzz import Fizzbuzz


def test_call_fizzBuzz():
    fizzbuzz = Fizzbuzz().Solution(15)
    assert fizzbuzz == 'FizzBuzz'


test_call_fizzBuzz()


def test_get_one():
    one = Fizzbuzz().Solution(1)
    assert one == "1"


test_get_one()


def test_get_two():
    two = Fizzbuzz().Solution(2)
    assert two == "2"


test_get_two()
