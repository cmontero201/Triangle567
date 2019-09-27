# -*- coding: utf-8 -*-
"""
Updated Jan 21, 2018
The primary goal of this file is to demonstrate a simple unittest implementation

@author: jrr
@author: rk
"""

import unittest

from Triangle import classify_triangle

# This code implements the unit test functionality
# https://docs.python.org/3/library/unittest.html has a nice description of the framework

class TestTriangles(unittest.TestCase):
    # define multiple sets of tests as functions with names that begin

    def testRightTriangleA(self): 
        self.assertEqual(classify_triangle(3,4,5),'Right','3,4,5 is a Right triangle')

    def testRightTriangleB(self): 
        self.assertNotEqual(classify_triangle(5,3,4),'Right','3,4,5 is a Right triangle')
        
    def testEquilateralTriangles(self): 
        self.assertEqual(classify_triangle(1,1,1),'Equilateral','1,1,1 should be equilateral')

    def testScaleneTriangles(self):
        self.assertEqual(classify_triangle(2,3,4), 'Scalene', '2,3,4 should be scalene')

    def testIsoscelesTriangles(self):
        self.assertEqual(classify_triangle(2,2,3), 'Isosceles', '2,2,3 should be isosceles')

    def testNonTriangles(self):
        self.assertEqual(classify_triangle(10,5,-2), 'InvalidInput', "Invalid")

    def testBounds(self):
        self.assertEqual(classify_triangle(201,201,201), "InvalidInput", "out of bounds")

    def testType(self):
        self.assertEqual(classify_triangle(201.55,201.55,201), "InvalidInput", "out of bounds")

if __name__ == '__main__':
    print('Running unit tests')
    unittest.main()

