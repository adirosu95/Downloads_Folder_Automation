"""
Test file extension_handler
Command line: python -m pytest tests\\utils\\file_extension_handler.py
"""

import pytest

from utils import file_extension_handler

@pytest.fixture
def arg_values():
    return {'file': r"C:\Users\edarosr\Downloads\Documents\20210122_183745289.pdf"}


def test_file_pdf(arg_values):
    assert file_extension_handler(arg_values['file']) == None


