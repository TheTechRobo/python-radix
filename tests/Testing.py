import unittest
from anyradix import *
from timeit import timeit

class TestRadixPerformance(unittest.TestCase):
    def test_perf(self):
        def testtime():
            for i in range(1000):
                cast(str(i), 16, 32)
        timeit(testtime, number=1000)

class TestRadixMethods(unittest.TestCase):

    def test_to_base_10(self):
        self.assertEqual(numeral_to_number('cfa7291', 25), 3080188976)

    def test_from_base_10(self):
        self.assertEqual(number_to_numeral(1465324, 15), '1de284')

    def test_cast(self):
        self.assertEqual(cast('51330od', 26, 36), 'privet')
        self.assertEqual(cast('privet', 36, 26), '51330od')
        self.assertEqual(cast(24, None, 12), '20')

    def test_from_base_10_exception(self):
        with self.assertRaises(Exception):
            number_to_numeral('a453', 12)

    def test_to_base_10_exception(self):
        with self.assertRaises(Exception):
            numeral_to_number('a453', 9)

    def test_cast_exception(self):
        with self.assertRaises(Exception):
            cast('9453', 9, 5)
        with self.assertRaises(Exception):
            cast('9453', 10, 100)

    def test_converter(self):
        self.assertEqual(Converter(4, 2).convert('3'), cast('3', 4, 2))
        self.assertEqual(Converter(None, 2).convert(3), cast(3, None, 2))

if __name__ == '__main__':
    unittest.main()
