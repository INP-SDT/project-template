# -*- coding: utf-8 -*-
"""Unit tests for the utils module.

This module contains tests to verify the correctness
of functions and classes defined in the utils module.

Author
------
Author Name

Date
----
YYYY-MM-DD
"""
import sys
from pathlib import Path
import unittest

sys.path.insert(
    0, str(Path(__file__).resolve().parent.parent / "src")
)

try:

    import mypackage

except:

    raise ImportError()


class TestCase(unittest.TestCase):

    def test_calculate(self):
        assert mypackage.utils.calculate(1, 2) == 3


if __name__ == '__main__':
    unittest.main()
