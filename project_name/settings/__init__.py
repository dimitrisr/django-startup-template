import os

try:
    from . import local
    from .development import *
except:
    from .production import *

