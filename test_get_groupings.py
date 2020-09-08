import unittest
from examples import scientists_search
from solver import get_horizontal, get_vertical, get_diagonal

class TestGetGroupings(unittest.TestCase):
    
    def test_get_horizontal(self) -> None:
        actual_answer = ['Y', 'T', 'R', 'V', 'R', 'I', 'U', 'R', 'O', 'U', 'T', 'O', 'A', 'R', 'A']
        func_answer = get_horizontal(scientists_search, (1, 4))
        self.assertEqual(actual_answer, func_answer)

    def test_get_vertical(self) -> None:
        actual_answer = ["D", "R", "A", "N", "R", "E", "B", "S", "S", "T", "Z", "I", "I", "T", "R"]
        func_answer = get_vertical(scientists_search, (1, 4))
        self.assertEqual(actual_answer, func_answer)

    def test_get_diagonals(self) -> None:
        left_to_right = ["E", "R", "E", "J", "J", "M", "H", "O", "B", "F", "T", "U"]
        right_to_left = ["I", "R", "G", "K", "O", "R"]
        actual_answer = (left_to_right, right_to_left)
        func_answer = get_diagonal(scientists_search, (1, 4))
        self.assertEqual(actual_answer, func_answer)

if __name__ == "__main__":
    unittest.main()