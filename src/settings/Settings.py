import sys
import os

INFINITY = sys.maxsize


def get_PROJECT_DIR():
    dir_path = os.path.dirname(os.path.realpath(__file__))
    return dir_path.rsplit("/", 2)[-3]
