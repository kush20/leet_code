import unittest
from main import Solution


class MyTestCase(unittest.TestCase):

    def test_sample1(self):
        the_wall = [1, 8, 6, 2, 5, 4, 8, 3, 7]
        s = Solution()
        area = s.max_area(the_wall)
        self.assertEqual(49, area)

    def test_sample2(self):
        the_wall = [4, 3, 2, 1, 4]
        s = Solution()
        area = s.max_area(the_wall)
        self.assertEqual(16, area)

    def test_sample3(self):
        the_wall = [1, 2, 1]
        s = Solution()
        area = s.max_area(the_wall)
        self.assertEqual(2, area)
