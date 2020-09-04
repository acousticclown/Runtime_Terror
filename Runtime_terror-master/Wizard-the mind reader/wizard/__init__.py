

from .wizard import wizard
from .exceptions import *
import os

__version__ = open(os.path.join(os.path.dirname(__file__), "VERSION.txt")).read()
