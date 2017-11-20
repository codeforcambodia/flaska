import os

_basedir = os.path.abspath(os.path.dirname(__file__))

class Default:
    PORT = 1031
class Development(Default):
    Debug=True
class Production(Default):
    pass
class Testing(Default):
    TESTING = True

config = {
    'DEFAULT':Default,
    'DEVELOPMENT': Development,
    'PRODUCTION': Production,
    'TESTING': Testing
}
