import os

try:
    import is_local
    from development import *
except:
    from production import *

