"""
TD
"""


from .main import handle_runs_default
from .main import form

# Define what should be available when using "from src import *"
__all__ = ['handle_runs_default', 'form']

# Package-level configuration
PACKAGE_NAME = 'everyday-template'
DEBUG = False

# Exclude test files from package imports
def _is_test_file(name: str) -> bool:
    return name.startswith("test_") or name.endswith("_test.py")
