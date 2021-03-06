'''Test script for Complex class.

Contains unit test for various operators on the class Complex from complex.py.
The unit test should be self-explanatory.
'''

from complex import Complex
from math import hypot

def test_eq_1():
    assert Complex(1,2) == Complex(1,2), \
            'Equality failed! False negative.'

def test_eq_1():
    assert Complex(1,2) != Complex(2,1), \
            'Equality failed! False positive.'

def test_eq_1():
    assert Complex(1,1) != Complex(1,2), \
            'Equality failed! False positive.'

def test_add_1():
    assert Complex(1,1) + Complex(2,2) == Complex(3,3), \
            'Addition failed! (1 + 1i) + (2 + 2i) != (3 + 3i)'

def test_add_2():
    assert Complex(2,-1) + Complex(-3,2) == Complex(-1,1), \
            'Addition failed! (2 - 1i) + (-3 + 2i) != (-1 + 1i)'

def test_add_3():
    assert Complex(-1,-1) + Complex(1,1) == Complex(0,0), \
            'Addition failed! (-1 - 1i) + (1 + 1i) != 0'

def test_subtract_1():
    assert Complex(1,1) - Complex(2,2) == Complex(-1,-1), \
            'Subtraction failed! (1 + 1i) - (2 + 2i) != (-1 - 1i)'

def test_subtract_2():
    assert Complex(2,-1) - Complex(-3,2) == Complex(5,-3), \
            'Subtraction failed! (2 - 1i) - (-3 + 2i) != (5 - 3i)'

def test_subtract_3():
    assert Complex(-1,-1) - Complex(1,1) == Complex(-2,-2), \
            'Subtraction failed! (-1 - 1i) - (1 + 1i) != (-2 - 2i)'

def test_conjugate_1():
    assert Complex(1,1).conjugate() == Complex(1,-1), \
            'Conjugation failed.'

def test_conjugate_2():
    assert Complex(0,3).conjugate() == Complex(0,-3), \
            'Conjugation failed.'

def test_conjugate_3():
    assert Complex(-2,-4).conjugate() == Complex(-2,4), \
            'Conjugation failed.'

def test_modulus_1():
    assert Complex(0,0).modulus() == 0, \
            'Modulus failed.'

def test_modulus_2():
    assert Complex(1,0).modulus() == 1, \
            'Modulus failed.'

def test_modulus_3():
    assert Complex(4,3).modulus() == 5, \
            'Modulus failed.'

def test_add_complex():
    assert Complex(2,3) + (2+2j) == Complex(4,5), \
            'Addition with python variant of complex numbers failed.'

def test_multiply_float():
    assert 4*Complex(3,4) == Complex(12,16), \
            'Multiplication of Complex by float failed.'

def test_multiply_float_subtract_float():
    assert 4*Complex(2,3) - 2 == Complex(6,12), \
            'Multiplication of Complex by float and subtraction of float failed.'

def test_float_subtract_complex():
    assert 2 - Complex(2,10) == Complex(0,-10), \
            'Subtraction of Complex by float failed.'

def test_eq_other():
    assert Complex(2,3) == (2+3j), \
            'Equality comparison with python complex failed.'
