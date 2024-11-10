import unittest
from math_quiz import function_A, function_B, function_C
class TestMathQuizFunctions(unittest.TestCase):

    # Test for function_A
    def test_function_A(self):
        # Example: function_A is expected to add two numbers
        result = function_A(2, 3)
        self.assertEqual(result, 5)  # Check if the result is correct

    # Test for function_B
    def test_function_B(self):
        # Example: function_B might be checking if a number is even
        result = function_B(4)
        self.assertTrue(result)  # Check if the result is True for even numbers

        result = function_B(5)
        self.assertFalse(result)  # Check if the result is False for odd numbers

    # Test for function_C
    def test_function_C(self):
        # Example: function_C could be returning the square of a number
        result = function_C(4)
        self.assertEqual(result, 16)  # Check if the square is correct

        result = function_C(0)
        self.assertEqual(result, 0)  # Edge case: check if the square of 0 is correct
if __name__ == '__main__':
    unittest.main()
