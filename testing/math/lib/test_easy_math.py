import unittest
from easy_math import calculate

class TestCalculate(unittest.TestCase):
    def test_calculate2plus1(self):
        self.assertEqual(calculate(2,1,'+'),3)
    def test_calculate2plus1IsNot(self):
        self.assertIsNot(calculate(2,1,'+'),4)
    def test_calculate2minus1(self):
        self.assertEqual(calculate(2,1,'-'),1)

if __name__ == '__main__':
    unittest.main()


