# -*- coding: utf-8 -*-
"""Example usage of the mypackage package.

Author
------
Author Name

Date
----
YYYY-MM-DD
"""
import sys
from pathlib import Path

sys.path.insert(
    0, str(Path(__file__).resolve().parent.parent / "src")
)

try:

    import mypackage

except:

    raise ImportError()

result = mypackage.utils.calculate(1, 2)
print(result)
