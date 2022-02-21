import unittest, my_math

class  SquareTestCase(unittest.TestCase):
    def test_square(self):
        for x in range(-10, 10):
            p = my_math.square(x)
            self.assertEqual(p, x * x, "テストに失敗しました")

if __name__ == "__main__":
    unittest.main()