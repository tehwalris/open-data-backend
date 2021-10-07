from pathlib import Path


def get_path_from_root(p):
    return Path(__file__).parent / ".." / p
