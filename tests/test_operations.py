'''
Tests these operations with a combination of
positive and negative ints and floats:
    - add
    - subtract
    - multiply
    - divide
        - division by zero error
'''
from typing import Union
import pytest
from app.operations import add, subtract, multiply, divide

Number = Union[int, float]

@pytest.mark.parametrize("a, b, expected", [
    (1, 2, 3),          # pos ints
    (-1, -2, -3),       # neg ints
    (3, -2, 1),         # pos and neg ints
    (0, 0, 0),          # zeroes
    (1.5, 2.5, 4.0),    # positive floats
    (-1.0, -2.0, -3.0), # negative floats
    (3.0, -2.0, 1.0),   # pos and neg floats
    (3, 2.0, 5.0),      # int and floats
    (1000, 1000, 2000), # large numbers
])

def test_addition(a: Number, b: Number, expected: Number) -> None:
    '''Tests addition with outputs listed above'''
    result = add(a,b)
    assert result == expected, f"Expected {a} + {b} = {expected}, but got {a} + {b} = {result}"

@pytest.mark.parametrize("a, b, expected", [
    (3, 2, 1),          # pos ints
    (-3, -2, -1),       # neg ints
    (3, -2, 5),         # pos and neg ints
    (0, 0, 0),          # zeroes
    (4.0, 2.5, 1.5),    # pos floats
    (-3.0, -2.0, -1.0), # neg floats
    (3.0, -2.0, 5.0),   # pos and neg floats
    (3, 2.0, 1.0),      # int and floats
    (2000, 1000, 1000), # large numbers
])

def test_subtraction(a: Number, b: Number, expected: Number) -> None:
    '''Tests subtraaction with outputs listed above'''
    result = subtract(a,b)
    assert result == expected, f"Expected {a} - {b} = {expected}, but got {a} - {b} = {result}"

@pytest.mark.parametrize("a, b, expected", [
    (2, 3, 6),              # pos ints
    (-2, -3, 6),            # neg ints
    (2, -3, -6),            # pos and neg ints
    (0, 0, 0),              # zeroes
    (2.0, 3.0, 6.0),        # pos floats
    (-2.0, -3.0, 6.0),      # neg floats
    (2.0, -3.0, -6.0),      # pos and neg floats
    (2, 3.0, 6.0),          # int and floats
    (2000, 3000, 6000000)   # large numbers
])

def test_multiplication(a: Number, b: Number, expected: Number) -> None:
    '''Tests multiplcation with outputs listed above'''
    result = multiply(a,b)
    assert result == expected, f"Expected {a} * {b} = {expected}, but got {a} * {b} = {result}"

@pytest.mark.parametrize("a, b, expected", [
    (6, 3, 2),              # pos ints
    (-6, -3, 2),            # neg ints
    (-6, 3, -2),            # pos and neg ints
    (6.0, 3.0, 2.0),        # pos ints
    (-6.0, -3.0, 2.0),      # neg floats
    (6.0, -3.0, -2.0),      # pos and neg floats
    (6, 3.0, 2.0),          # int and floats
    (6000000, 3000, 2000)   # large numbers
])

def test_division(a: Number, b: Number, expected: Number) -> None:
    '''Tests division with outputs listed above'''
    result = divide(a,b)
    assert result == expected, f"Expected {a} / {b} = {expected}, but got {a} / {b} = {result}"

def test_division_by_zero() -> None:
    '''Tests that dividing by zero raises ValueError'''
    with pytest.raises(ValueError, match="Cannot divide by zero."):
        divide(1,0)         # pos ints
        divide(-1,0)        # neg ints
        divide(1.0, 0.0)    # pos floats
        divide(-1.0, 0.0)   # neg floats
        divide(1, 0.0)      # int and float
        divide(1000, 0)     # large numbers
