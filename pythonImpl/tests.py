import unittest
from aStarAlgorithm import aStarAlgorithm, firstNode


class TestAStarAlgorithm(unittest.TestCase):

    def test_output(self):
        self.assertEqual(aStarAlgorithm(firstNode(
            " 5 1 2 3 9  6 7 4  13 10 11   8 0 14 15 12")), 9)
        self.assertEqual(aStarAlgorithm(firstNode("2 3 0 8 1 5 4 7 9  6 10 12 13 14 11  15")),
                         12)
        self.assertEqual(aStarAlgorithm(firstNode(
            " 9 5 1 0 13 6 7 2 14 10 11 3 15 12 8  4")), 27)
        self.assertEqual(aStarAlgorithm(firstNode(" 0 1 3 4 5 2 6 8 9 10 7 11 13 14 15 12")),
                         6)


if __name__ == '__main__':
    unittest.main()
