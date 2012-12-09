import os

try:
    import app.is_local
    from development import *
except:
    from production import *

