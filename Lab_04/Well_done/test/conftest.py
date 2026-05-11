"""
conftest.py - общая конфигурация pytest для Lab_04.

Автоматически добавляет папку Rare в PYTHONPATH,
чтобы импорты "from common import ..." работали,
как при запуске Lab_04/Rare/Main.py

"""

import sys
from pathlib import Path


def pytest_configure() -> None:
    """Выполняется один раз при старте pytest."""
    rare_path = Path(__file__).parent.parent.parent / "Rare"
    if str(rare_path) not in sys.path:
        sys.path.insert(0, str(rare_path))