"""Make the lab's modules importable for the test files.

In the student repository, ``tests/`` sits beside ``q2.py`` at the
project root, so the project root goes on sys.path.
When the tests run against the instructor's reference solutions, the
optional ``solution/`` directory is added as well.
"""

import sys
from pathlib import Path

_root = Path(__file__).resolve().parent.parent
for _path in (_root, _root / "solution"):
    if _path.is_dir() and str(_path) not in sys.path:
        sys.path.insert(0, str(_path))
