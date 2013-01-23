#-*- coding: utf-8 -*-
u'''
Test exercise 0: mutable and immutable types common errors
'''
import unittest
import exercise_0
# import solution_0 as exercise_0


class VerboseTestCase(unittest.TestCase):
    '''Base unit tests class for verbose output
    '''
    @classmethod
    def setUpClass(cls):
        cls.maxDiff = None
        cls.longMessage = True


class TestMutableImmutable(VerboseTestCase):
    '''Test exercise 0: mutable and immutable types common errors
    '''
    def test_split_even_odd(self):
        '''Check multiple assignment of mutables
        '''
        numbers = range(0, 16)
        expected_even = range(0, 16, 2)
        expected_odd = range(1, 16, 2)
        even, odd = exercise_0.split_even_odd(numbers)
        self.assertEqual(even, expected_even, "Even values differ")
        self.assertEqual(odd, expected_odd, "Odd values differ")

    def test_append_number_even(self):
        '''Check mutable class attributes
        '''
        inst = exercise_0.NumbersList()
        number = 6
        expected_even = [number]
        expected_odd = []
        inst.append_number(number)
        self.assertEqual(inst.even, expected_even, "Even values differ")
        self.assertEqual(inst.odd, expected_odd, "Odd values differ")

    def test_append_number_odd(self):
        '''Check mutable as class attributes
        '''
        inst = exercise_0.NumbersList()
        number = 7
        expected_even = []
        expected_odd = [number]
        inst.append_number(number)
        self.assertEqual(inst.even, expected_even, "Even values differ")
        self.assertEqual(inst.odd, expected_odd, "Odd values differ")

    def test_update_even_odd_I(self):
        '''Check mutable as default value I
        '''
        numbers = range(0, 16)
        expected_even = range(0, 16, 2)
        expected_odd = range(1, 16, 2)
        even, odd = exercise_0.update_even_odd(numbers)
        self.assertEqual(even, expected_even, "Even values differ")
        self.assertEqual(odd, expected_odd, "Odd values differ")

    def test_update_even_odd_II(self):
        '''Check mutable as default value II
        '''
        numbers = range(1, 17)
        expected_even = range(2, 17, 2)
        expected_odd = range(1, 17, 2)
        even, odd = exercise_0.update_even_odd(numbers)
        self.assertEqual(even, expected_even, "Even values differ")
        self.assertEqual(odd, expected_odd, "Odd values differ")


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()