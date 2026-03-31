import io
import unittest
from contextlib import redirect_stdout

from main import pick_random_numbers, print_random_numbers


class RandomNumberTests(unittest.TestCase):
    def test_pick_random_numbers_returns_20_unique_values_in_range(self):
        numbers = pick_random_numbers()

        self.assertEqual(len(numbers), 20)
        self.assertEqual(len(set(numbers)), 20)
        self.assertTrue(all(1 <= number <= 100 for number in numbers))

    def test_print_random_numbers_prints_generated_values(self):
        buffer = io.StringIO()

        with redirect_stdout(buffer):
            numbers = print_random_numbers()

        printed_numbers = [int(value) for value in buffer.getvalue().strip().split()]
        self.assertEqual(printed_numbers, numbers)


if __name__ == "__main__":
    unittest.main()
