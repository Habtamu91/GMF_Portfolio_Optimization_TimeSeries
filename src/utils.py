# src/utils.py
import os

def get_project_root():
    """Returns the absolute path to the project root folder"""
    return os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

def make_path_relative_to_root(*path_parts):
    """Constructs absolute paths relative to project root"""
    return os.path.join(get_project_root(), *path_parts)