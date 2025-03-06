class Complex:
    def __init__(self, real=0, imag=0):
        self.real = real
        self.imag = imag

    @property
    def real(self):
        return self._real

    @real.setter
    def real(self, value):
        try:
            _ = value + 0
        except TypeError:
            raise TypeError("Real must be a number")
        self._real = value

        #dont try TypeError, raise TypeError

    @property
    def imag(self):
        return self._imag

    @imag.setter
    def imag(self, value):
        try:
            _ = value + 0
        except TypeError:
            raise TypeError("Imaginary must be a number")
        self._imag = value

    @property
    def reciprocal(self):
        denom = self.real ** 2 + self.imag ** 2
        if denom == 0:
            raise ZeroDivisionError("Cannot compute reciprocal of zero complex number")
        return Complex(self.real / denom, -self.imag / denom)

    def __str__(self):
        return f"({self.real}, {self.imag})"

    def __neg__(self):
        return Complex(-self.real, -self.imag)

    def __add__(self, other):
        try:
            return Complex(self.real + other.real, self.imag + other.imag)
        except AttributeError:
            raise TypeError(f"Unsupported operand type for +: {type(other)}")

    def __radd__(self, other):
        return self + other

    def __sub__(self, other):
        try:
            return Complex(self.real - other.real, self.imag - other.imag)
        except AttributeError:
            raise TypeError(f"Unsupported operand type for -: {type(other)}")

    def __rsub__(self, other):
        try:
            return Complex(other.real, other.imag) - self
        except AttributeError:
            raise TypeError(f"Unsupported operand type for -: {type(other)}")

    def __mul__(self, other):
        try:
            s_real = other.real
            s_imag = other.imag
        except AttributeError:
            raise TypeError(f"Unsupported operand type for *: {type(other)}")
        real_part = self.real * s_real - self.imag * s_imag
        imag_part = self.real * s_imag + self.imag * s_real
        return Complex(real_part, imag_part)

    def __rmul__(self, other):
        return self * other

    def __truediv__(self, other):
        try:
            other_real = other.real
            other_imag = other.imag
        except AttributeError:
            raise TypeError(f"Unsupported operand type for /: {type(other)}")
        other_complex = Complex(other_real, other_imag)
        return self * other_complex.reciprocal

    def __rtruediv__(self, other):
        try:
            other_real = other.real
            other_imag = other.imag
        except AttributeError:
            raise TypeError(f"Unsupported operand type for /: {type(other)}")
        other_complex = Complex(other_real, other_imag)
        return other_complex / self

    def __abs__(self):
        return (self.real ** 2 + self.imag ** 2) ** 0.5

    def __eq__(self, other):
        try:
            return (self.real == other.real) and (self.imag == other.imag)
        except AttributeError:
            try:
                return self.real == other.real and self.imag == other.imag
            except AttributeError:
                return False

    def __lt__(self, other):
        try:
            other_complex = Complex(other.real, other.imag)
        except (AttributeError, TypeError):
            raise TypeError(f"Unsupported operand type for <: {type(other)}")
        return abs(self) < abs(other_complex)