import unittest
from anyradix import *
from timeit import timeit

class TestRadixPerformance(unittest.TestCase):
    def test_perf(self):
        def testtime():
            for i in range(1000):
                cast(i, 16, 32)
        timeit(testtime, number=1000)

class TestRadixMethods(unittest.TestCase):

    def test_cast(self):
        self.assertEqual(cast('51330od', 26, 36), 'privet')
        self.assertEqual(cast('privet', 36, 26), '51330od')
        self.assertEqual(cast(0, 10, 12), '0')
        self.assertEqual(cast('0', 10, 12), '0')
        self.assertEqual(cast('', 10, 12), '0')
        self.assertEqual(cast('12', 8, 12), 'a')
        self.assertEqual(cast(12, 8, 12), '10')
        self.assertEqual(cast(12, 10, 12), cast('12', 10, 12))
        self.assertNotEqual(cast(12, 8, 12), cast('12', 8, 12))

    def test_cast_exception(self):
        with self.assertRaises(Exception):
            cast('9453', 9, 5)
        with self.assertRaises(Exception):
            cast('9453', 10, 1)
        with self.assertRaises(Exception):
            cast('9453', 10, 37)
        with self.assertRaises(Exception):
            cast('-9453', 10, 12)
        with self.assertRaises(Exception):
            cast(-9453, 10, 12)

if __name__ == '__main__':
    unittest.main()
