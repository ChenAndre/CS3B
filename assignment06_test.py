import unittest

class TestComplex(unittest.TestCase):
    def setUp(self):
        self.c1 = Complex(1, 2)
        self.c2 = Complex(3, 4)
        self.num = 10
        self.fnum = 5.5

    def test_addition(self):
        result = self.c1 + self.c2
        self.assertAlmostEqual(result.real, 4)
        self.assertAlmostEqual(result.imag, 6)
        result = self.c1 + self.num
        self.assertAlmostEqual(result.real, 11)
        self.assertAlmostEqual(result.imag, 2)
        result = self.num + self.c1
        self.assertAlmostEqual(result.real, 11)
        self.assertAlmostEqual(result.imag, 2)
        with self.assertRaises(TypeError):
            self.c1 + 'invalid'

    def test_subtraction(self):
        result = self.c2 - self.c1
        self.assertAlmostEqual(result.real, 2)
        self.assertAlmostEqual(result.imag, 2)
        result = self.c2 - self.num
        self.assertAlmostEqual(result.real, -7)
        self.assertAlmostEqual(result.imag, 4)
        result = self.num - self.c1
        self.assertAlmostEqual(result.real, 9)
        self.assertAlmostEqual(result.imag, -2)
        with self.assertRaises(TypeError):
            self.c1 - 'invalid'

    def test_multiplication(self):
        result = self.c1 * self.c2
        self.assertAlmostEqual(result.real, -5)
        self.assertAlmostEqual(result.imag, 10)
        result = self.c1 * self.num
        self.assertAlmostEqual(result.real, 10)
        self.assertAlmostEqual(result.imag, 20)
        result = self.num * self.c1
        self.assertAlmostEqual(result.real, 10)
        self.assertAlmostEqual(result.imag, 20)
        with self.assertRaises(TypeError):
            self.c1 * 'invalid'

    def test_division(self):
        result = self.c1 / self.c2
        self.assertAlmostEqual(result.real, 0.44)
        self.assertAlmostEqual(result.imag, 0.08)
        result = self.c1 / self.num
        self.assertAlmostEqual(result.real, 0.1)
        self.assertAlmostEqual(result.imag, 0.2)
        c = Complex(5, 0)
        result = self.num / c
        self.assertAlmostEqual(result.real, 2)
        self.assertAlmostEqual(result.imag, 0)
        with self.assertRaises(ZeroDivisionError):
            self.c1 / Complex(0, 0)
        with self.assertRaises(TypeError):
            self.c1 / 'invalid'

    def test_reciprocal(self):
        c = Complex(3, 4)
        recip = c.reciprocal
        self.assertAlmostEqual(recip.real, 0.12)
        self.assertAlmostEqual(recip.imag, -0.16)
        with self.assertRaises(ZeroDivisionError):
            Complex(0, 0).reciprocal

    def test_abs(self):
        self.assertAlmostEqual(abs(self.c2), 5)

    def test_equality(self):
        self.assertTrue(Complex(5, 0) == 5)
        self.assertTrue(Complex(5, 0) == 5.0)
        self.assertTrue(Complex(5, 0) == Complex(5, 0))
        self.assertFalse(Complex(5, 1) == 5)
        self.assertFalse(Complex(5, 0) == '5')

    def test_less_than(self):
        self.assertTrue(Complex(3, 4) < 6)
        self.assertFalse(Complex(5, 0) < 5)
        self.assertFalse(Complex(6, 0) < 5)
        with self.assertRaises(TypeError):
            Complex(1, 2) < 'invalid'

    def test_shallow_copy(self):
        original = [self.c1, self.c2]
        copied = copy.copy(original)
        self.assertIsNot(copied, original)
        for o, c in zip(original, copied):
            self.assertIs(o, c)

    def test_deep_copy(self):
        original = [self.c1, self.c2]
        copied = copy.deepcopy(original)
        self.assertIsNot(copied, original)
        for o, c in zip(original, copied):
            self.assertIsNot(o, c)
            self.assertEqual(o.real, c.real)
            self.assertEqual(o.imag, c.imag)

if __name__ == '__main__':
    unittest.main()