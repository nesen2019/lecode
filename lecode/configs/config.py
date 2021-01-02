import os

class ConfigLecode:
    def __init__(self):
        self.PROJECT_ROOT = __file__
        for i in range(3):
            self.PROJECT_ROOT = os.path.dirname(self.PROJECT_ROOT)

cfg = ConfigLecode()


