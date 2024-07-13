# test_simple_calculator.py

import unittest
from simple_calculator import SimpleCalculator

class TestSimpleCalculator(unittest.TestCase):
    """Unit tests for the SimpleCalculator class."""

    def setUp(self):
        """Set up the SimpleCalculator instance before each test."""
        self.calc = SimpleCalculator()

    def test_addition(self):
        """Test the addition method."""
        self.assertEqual(self.calc.add(2, 3), 5, "Addition of 2 and 3 should be 5")
        self.assertEqual(self.calc.add(-1, 1), 0, "Addition of -1 and 1 should be 0")
        self.assertEqual(self.calc.add(0, 0), 0, "Addition of 0 and 0 should be 0")
        self.assertEqual(self.calc.add(-1, -1), -2, "Addition of -1 and -1 should be -2")
        self.assertEqual(self.calc.add(1.5, 2.5), 4.0, "Addition of 1.5 and 2.5 should be 4.0")

    def test_subtraction(self):
        """Test the subtraction method."""
        self.assertEqual(self.calc.subtract(5, 3), 2, "Subtraction of 5 from 3 should be 2")
        self.assertEqual(self.calc.subtract(-1, 1), -2, "Subtraction of 1 from -1 should be -2")
        self.assertEqual(self.calc.subtract(0, 0), 0, "Subtraction of 0 from 0 should be 0")
        self.assertEqual(self.calc.subtract(-1, -1), 0, "Subtraction of -1 from -1 should be 0")
        self.assertEqual(self.calc.subtract(2.5, 1.5), 1.0, "Subtraction of 1.5 from 2.5 should be 1.0")

    def test_multiplication(self):
        """Test the multiplication method."""
        self.assertEqual(self.calc.multiply(2, 3), 6, "Multiplication of 2 and 3 should be 6")
        self.assertEqual(self.calc.multiply(-1, 1), -1, "Multiplication of -1 and 1 should be -1")
        self.assertEqual(self.calc.multiply(0, 5), 0, "Multiplication of 0 and 5 should be 0")
        self.assertEqual(self.calc.multiply(-1, -1), 1, "Multiplication of -1 and -1 should be 1")
        self.assertEqual(self.calc.multiply(1.5, 2.0), 3.0, "Multiplication of 1.5 and 2.0 should be 3.0")

    def test_division(self):
        """Test the division method."""
        self.assertEqual(self.calc.divide(6, 2), 3, "Division of 6 by 2 should be 3")
        self.assertEqual(self.calc.divide(-4, 2), -2, "Division of -4 by 2 should be -2")
        self.assertEqual(self.calc.divide(5, 2), 2.5, "Division of 5 by 2 should be 2.5")
        self.assertEqual(self.calc.divide(0, 1), 0, "Division of 0 by 1 should be 0")
        self.assertEqual(self.calc.divide(-5, -2), 2.5, "Division of -5 by -2 should be 2.5")
        self.assertIsNone(self.calc.divide(1, 0), "Division by zero should return None")

    def test_division_with_large_numbers(self):
        """Test the division method with large numbers."""
        self.assertEqual(self.calc.divide(10**6, 10**3), 10**3, "Division of 10^6 by 10^3 should be 10^3")
        self.assertEqual(self.calc.divide(10**6, 1), 10**6, "Division of 10^6 by 1 should be 10^6")

    def test_division_with_float_numbers(self):
        """Test the division method with floating-point numbers."""
        self.assertEqual(self.calc.divide(7.0, 2.0), 3.5, "Division of 7.0 by 2.0 should be 3.5")
        self.assertEqual(self.calc.divide(1.5, 0.5), 3.0, "Division of 1.5 by 0.5 should be 3.0")

if __name__ == '__main__':
    unittest.main()

