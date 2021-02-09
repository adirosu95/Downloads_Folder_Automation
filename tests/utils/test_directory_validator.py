"""
Test directory validator
Command line: python -m pytest tests\\utils\\directory_validator.py
"""

import pytest

from utils import directory_validator


@pytest.fixture
def arg_values():
    return {
        'parent_dir': r'C:\\Users\\edarosr\\Google Drive\\Personal_Space_Drive\\'
                      r'Python_Projects\\02_Downloads_Folder_Automation',
        'dir_name': 'Intel',
    }


@pytest.mark.parametrize('parent_dir,exception',
                         [(r'C:\\Users\\edarosr\\Google Drive\\Personal_Space_Drive\\'
                           r'Python_Projects\\03_Downloads_Folder_Automation', ValueError),
                          (123, TypeError)])
def test_parent_dir(parent_dir, exception, arg_values):
    arg_values['parent_dir'] = parent_dir
    with pytest.raises(exception):
        directory_validator(**arg_values)


@pytest.mark.parametrize('dir_name,exception', [(123, TypeError)])
def test_dir_name(dir_name, exception, arg_values):
    arg_values['dir_name'] = dir_name
    with pytest.raises(exception):
        directory_validator(**arg_values)


def test_directory_validator_pass(arg_values):
    assert directory_validator(**arg_values) is None
