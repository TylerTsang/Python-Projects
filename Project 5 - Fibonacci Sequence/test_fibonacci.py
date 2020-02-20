# -*- coding: utf-8 -*-
#Fibonacci Sequence Unit Test

import unittest
from fibonacci import Fibonacci_Sequence

class TestFibonacci(unittest.TestCase):
    def test_sequence(self):
        # Test for numbers >= 1
        self.assertAlmostEqual(Fibonacci_Sequence(1), 1)
        self.assertAlmostEqual(Fibonacci_Sequence(4), 3)
        self.assertAlmostEqual(Fibonacci_Sequence(7), 13)
        
    def test_values(self):
        # Make sure errors are raised if negative
        self.assertRaises(ValueError, Fibonacci_Sequence, -3)
        
    def test_types(self):
        # Make sure errors are raised if value input is not an integer
        self.assertRaises(TypeError, Fibonacci_Sequence, 3+7j)
        self.assertRaises(TypeError, Fibonacci_Sequence, True)
        self.assertRaises(TypeError, Fibonacci_Sequence, 'word')
        self.assertRaises(TypeError, Fibonacci_Sequence, 2.1)
    