'''
Contains arithmetic operations:
    - add
    - subtract
    - multiply
    - divide
        - Raises error if user attempts to divide by zero.

All inputs are type-hinted to be ints or floats.
'''
from typing import Union

Number = Union[int, float]

def add(a: Number, b: Number) -> Number:
    '''Adds two numbers and returns the result'''
    result = a + b
    return result

def subtract(a: Number, b: Number) -> Number:
    '''Subtracts two numbers and returns the result'''
    result = a - b
    return result

def multiply(a: Number, b: Number) -> Number:
    '''Multiplies two numbers and returns the result.'''
    result = a * b
    return result

def divide(a: Number, b: Number) -> Number:
    '''
    Divides two numbers and returns the result.
    Raises a ValueError for division by zero.
    '''
    if b == 0:
        raise ValueError("Cannot divide by zero.")
    result = a / b
    return result
