"""Directory validator"""

import os


def directory_validator(parent_dir, dir_name):
    """
    Check if 'dir_path' exists, if not, will create the directory.
    Args:
        dir_name (str): directory name being checked
        parent_dir (str): the parent directory path
    Returns:
        None: no exception raised if validation passes
    Raises:
        TypeError: if 'parent_dir' or 'dir_name' are not strings
        ValueError: if 'parent_dir' is not a valid path
    """
    if not isinstance(parent_dir, str):
        raise TypeError(f"{parent_dir} must be a string type.")

    if not isinstance(dir_name, str):
        raise TypeError(f"{dir_name} must be a string type.")

    if not os.path.exists(parent_dir):
        raise ValueError(f"{parent_dir} must be a valid path.")

    all_directories = (d for d in os.listdir(parent_dir) if os.path.isdir(os.path.join(parent_dir, d)))
    if dir_name not in all_directories:
        os.mkdir(os.path.join(parent_dir, dir_name))
