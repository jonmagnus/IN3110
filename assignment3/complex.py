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
            other (Complex): The other complex number to compare with.

        Returns:
            bool: True if the numbers are equal. False otherwise.
        '''
        return self.a == other.a and self.b == other.b
    
    def __add__(self,other):
        '''Addition operatot
        Args:
            other (Complex): The second complex number to add.

        Returns:
            Complex: The sum of the two complex numbers.
        '''
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
            other (Complex): The second complex number to subtract from the first (self).

        Returns:
            Complex: The difference of the two complex numbers.
        '''
        return self + (-other)

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
