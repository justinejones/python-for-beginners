""" Test file for writing_files module"""
import pytest
import datetime
from pathlib import Path
from src.utilities.file_processing import reading_files, writing_files
path = Path(__file__).parent.absolute()


def test_writing_json_files():
    """Tests reading a json file.

    :raises:

    :rtype:
    """
    x = datetime.datetime.now()
    content = {
        "test_file": [
            {
                "test_key": "testValue"
            }
        ]
    }
    file_name = f"/test_writing_json_file_{x}.json"
    full_path = f"{path}{file_name}"
    writing_files.write_json_file(full_path, content)
    response = reading_files.read_json_file(full_path)
    assert response
    assert response == content
