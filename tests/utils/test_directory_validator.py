"""
Test directory validator
Command line: python -m pytest tests\\utils\\directory_validator.py
"""

import pytest

from app.utils.directory_validator import check_directory


@pytest.fixture
def resource_values():
    return {
        'parent_dir': r'C:\\Users\\edarosr\\Google Drive\\Personal_Space_Drive\\Python_Projects\\02_Downloads_Folder_Automation',
        'dir_name': 'Intel',
    }
