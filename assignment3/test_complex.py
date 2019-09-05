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
    assert Complex(2,3).modulus() == 5, \
            'Modulus failed.'
