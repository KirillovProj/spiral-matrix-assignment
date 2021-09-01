import unittest
import spiral_algorithm

class TestSpiralAlgo(unittest.TestCase):

    def test_right_answer(self):
        input = [10, 20, 30, 40,
                 50, 60, 70, 80,
                 90, 100, 110, 120,
                 130, 140, 150, 160]
        right_answer = [
                10, 50, 90, 130,
                140, 150, 160, 120,
                80, 40, 30, 20,
                60, 100, 110, 70]
        result = spiral_algorithm.counter_clock_spiral(input, 4)
        self.assertEqual(result, right_answer)

    def test_empty_matrix(self):
        input = []
        result = spiral_algorithm.counter_clock_spiral(input, 0)
        self.assertEqual(result, 'Empty matrix passed')

    def test_single_number_matrix(self):
        input = [1]
        right_answer = [1]
        result = spiral_algorithm.counter_clock_spiral(input, 1)
        self.assertEqual(result, right_answer)

