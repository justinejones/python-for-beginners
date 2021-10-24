""" Test file for reading_files module"""
import pytest
from pathlib import Path
from src.utilities.file_processing import reading_files
path = Path(__file__).parent.absolute()


def test_reading_json_files():
    """Tests reading a json file.

    :raises:

    :rtype:
    """
    response = reading_files.read_json_file(f"{path}/json_test_file.json")
    assert response
