import pytest
from lib.Fizzbuzz import Fizzbuzz

def test_call_fizzBuzz():
    fizzbuzz = Fizzbuzz().Solution(15)
    assert fizzbuzz == "FizzBuzz"
test_call_fizzBuzz()

def test_get_one():
    one = Fizzbuzz().Solution(1)
    assert one == "1"
test_get_one()

def test_get_two():
    two = Fizzbuzz().Solution(2)
    assert two == "2"
test_get_two()

def test_get_three():
    three = Fizzbuzz().Solution(3)
    assert three == "Fizz"
test_get_three()

def test_get_five():
    five = Fizzbuzz().Solution(5)
    assert five == "Buzz"
test_get_five()

def test_get_six():
    six = Fizzbuzz().Solution(6)
    assert six == "Fizz"
test_get_six()

def test_get_ten():
    ten = Fizzbuzz().Solution(10)
    assert ten == "Buzz"
test_get_ten()

def test_get_Fizzbuzz():
    fizzbuzz = Fizzbuzz().Solution(15)
    assert fizzbuzz == "FizzBuzz"
test_get_Fizzbuzz()