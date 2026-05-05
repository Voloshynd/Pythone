import os

def get_path(path):
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    ABSOLUTE_PATH = os.path.join(BASE_DIR, path)
    return ABSOLUTE_PATH