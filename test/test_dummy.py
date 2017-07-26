'''
File: test_dummy.py
Author: Zachary King

Implements a dummy unit test to get
testing up and off the ground :)
'''

import unittest

class TestHelloWorld(unittest.TestCase):
    def test_true(self):
        self.assertTrue(True)

if __name__ == '__main__':
    unittest.main()
