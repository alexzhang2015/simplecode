import unittest
from array import Solution

class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_removeDuplicates(self):
        test_cases = [
            {'input': [1, 1, 2], 'output': 2},
            {'input': [0, 0, 1, 1, 1, 2, 2, 3, 3, 4], 'output': 5},
            {'input': [], 'output': 0},
            # add more test cases
        ]

        for case in test_cases:
            with self.subTest(case=case):
                self.assertEqual(self.solution.removeDuplicates(case['input']), case['output'])


if __name__ == '__main__':
    unittest.main()