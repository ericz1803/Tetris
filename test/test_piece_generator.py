import unittest
import numpy as np
from tetris import piece_generator

#only tests grab bag style of piece generation
class TestPieceGenerator(unittest.TestCase):
    def setUp(self):
        self.grab_bag = piece_generator.GrabBag()

    #grab bag should return 1 of each piece until all of them run out
    def test_uniqueness(self):
        pieces = list()
        for _ in range(7):
            pieces.append(self.grab_bag.next())

        self.assertEqual(len(set(pieces)), 7, 'returned duplicate piece')

    def test_return_int(self):
        self.assertTrue(np.issubdtype(self.grab_bag.next(), np.integer), 'next function did not return an integer')

        self.assertTrue(type(self.grab_bag.next_with_preview()) is tuple, 'next_with_preview function did not return a tuple')
        self.assertTrue(np.issubdtype(self.grab_bag.next_with_preview()[0], np.integer), 'expected a tuple of integers')
        self.assertTrue(np.issubdtype(self.grab_bag.next_with_preview()[1], np.integer), 'expected a tuple of integers')

if __name__ == '__main__':
    unittest.main()
