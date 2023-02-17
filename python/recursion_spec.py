# Write your unit tests here
from recursion_challenge import factorial, palindrome, bottles, roman_num
import unittest, math

class RecursionTester(unittest.TestCase):

    def test_factorial(self):
        """All tests for factorial"""
        test_number = 5
        edge_case = [1, 0]
        self.assertEqual(factorial(test_number), math.factorial(test_number))
        for num in edge_case:
            self.assertEqual(factorial(num), math.factorial(num))

    def test_palindrome(self):
        """All tests for palindrome"""
        test_case = 'racecar'
        false_case = 'not a palindrome'
        edge = 'Sore was I ere I saw Eros.'
        self.assertEqual(palindrome(test_case), True)
        self.assertEqual(palindrome(false_case), False)
        self.assertEqual(palindrome(edge), True)

    def test_bottles(self):
        """All tests for bottles"""
        test_case = 5

        self.assertIsNotNone(bottles(test_case))

    def test_roman(self):
        """All tests for roman numerals"""
        self.assertEqual(roman_num(1), 'I')
        self.assertEqual(roman_num(4), 'IV')


if __name__ == "__main__":
    unittest.main()