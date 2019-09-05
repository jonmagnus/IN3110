from math import hypot

class Complex:
    '''An implementation of complex numbers.
    Args:
        a (float): The real part of the complex number.
        b (float): The imaginary part of the complex number.

    Attributes:
        a (float): The real part of the complex number.
        b (float): The imaginary part of the complex number.
    '''
    def __init__(self,a,b):
        self.a = a
        self.b = b

    def __eq__(self,other):
        '''Equality operator
        Args:
            other (Complex, complex or float): The other complex number to compare with.

        Returns:
            bool: True if the numbers are equal. False otherwise.
        '''
        if not isinstance(other,Complex):
            other = complex(other)
            other = Complex(other.real, other.imag)
        return self.a == other.a and self.b == other.b
    
    def __add__(self,other):
        '''Addition operatot
        Args:
            other (Complex, complex or float): The second complex number to add.

        Returns:
            Complex: The sum of the two complex numbers.
        '''
        print(type(other))
        if not isinstance(other,Complex):
            return other + self
        return Complex(self.a + other.a, self.b + other.b)
    
    def __neg__(self):
        '''Negation operator
        Returns:
            Complex: The corresponding complex number with the signs of a and b reversed.
        '''
        return Complex(-self.a,-self.b)

    def __sub__(self,other):
        '''Subtraction operator
        Args:
            other (Complex, complex or float): The second complex number to subtract from the first (self).

        Returns:
            Complex: The difference of the two complex numbers.
        '''
        if not isinstance(other,Complex):
            return -(other - self)
        return self + (-other)
    
    def __mul__(self,other):
        '''Multiplication operator
        Args:
            other (Complex, complex or float): The second complex number to multiply the first (self) by.

        Returns:
            Complex: The product of the multiplication.
        '''
        if not isinstance(other,Complex):
            return other * self
        return Complex(self.a*other.a - self.b*other.b, self.a*other.b + self.b*other.a)
    
    def __radd__(self,other):
        '''Right addition operator
        Args:
            other (float or complex): A number of type other than Complex to be added.
        Returns:
            Complex: The sum.
        '''
        other = complex(other)
        return self + Complex(other.real,other.imag)
    
    def __rsub__(self,other):
        '''Right subtraction operator
        Args:
            other (float or complex): A number of type other than Complex to be subtracted.
        Returns:
            Complex: The difference.
        '''
        other = complex(other)
        return Complex(other.real,other.imag) - self
    
    def __rmul__(self,other):
        '''Right multiplication operator
        Args:
            other (float or complex): A number of type other than Complex to be multiplied.
        Returns:
            Complex: The product.
        '''
        other = complex(other)
        return self * Complex(other.real,other.imag)

    def conjugate(self):
        '''Conjugation operator
        Returns:
            Complex: The complex conjugate of self.
        '''
        return Complex(self.a,-self.b)
    
    def modulus(self):
        '''Modulus operator
        Returns:
            float: The modulus of self.
        '''
        return hypot(self.a,self.b)
