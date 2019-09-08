# -*- coding: utf-8 -*-
"""
Updated Jan 21, 2018
The primary goal of this file is to demonstrate a simple unittest implementation

@author: jrr
@author: rk
"""

import unittest

from Triangle import classifyTriangle

# This code implements the unit test functionality
# https://docs.python.org/3/library/unittest.html has a nice description of the framework

class TestTriangles(unittest.TestCase):
    # define multiple sets of tests as functions with names that begin

    def testRightTriangleA(self): 
        self.assertEqual(classifyTriangle(3,4,5),'Right','3,4,5 is a Right triangle')

    def testRightTriangleB(self): 
        self.assertEqual(classifyTriangle(5,3,4),'Scalene','5,3,4 is NOT a Right triangle')
        
    def testEquilateralTriangles(self): 
        self.assertEqual(classifyTriangle(1,1,1),'Equilateral','1,1,1 is equilateral')

    def testScaleneTriangles(self):
        self.assertEqual(classifyTriangle(2,3,4), 'Scalene', '2,3,4 is scalene')

    def testIsoscelesTriangles(self):
        self.assertEqual(classifyTriangle(5,5,4), 'Isosceles', '2,2,5 is isosceles')

    def testNonTriangles(self):
        self.assertEqual(classifyTriangle(10,5,-2), 'InvalidInput', "Is not a triangle")

    def testNonTrianglesB(self):
        self.assertEqual(classifyTriangle(10,5,100), 'NotATriangle', "Is not a triangle")
if __name__ == '__main__':
    print('Running unit tests')
    
    suite = unittest.TestLoader().loadTestsFromTestCase(TestTriangles)
    unittest.TextTestRunner(verbosity = 2).run(suite)
    
    unittest.main()

