import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "src"))

from example import add  # noqa: E402


class AddTest(unittest.TestCase):
    def test_adds_two_integers(self) -> None:
        self.assertEqual(add(2, 3), 5)

    def test_negative_numbers(self) -> None:
        self.assertEqual(add(-4, 1), -3)


if __name__ == "__main__":
    unittest.main()
