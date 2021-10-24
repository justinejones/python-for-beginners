""" Test file for writing_files module"""
import pytest
import datetime
from pathlib import Path
from src.utilities.file_processing import reading_files, writing_files
path = Path(__file__).parent.absolute()


def test_writing_json_files():
    """Tests writing a json file.

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


def test_writing_csv_files():
    """Tests writing a csv file.

    :raises:

    :rtype:
    """
    x = datetime.datetime.now()
    headers = ["Header1", "Header2", "Header3"]
    content = [["Column1", "Column2", "Column3"],
               ["Row2C1", "Row2C2", "Row2C3"],
               ["Row3C1", "Row3C2", "Row3C3"]
               ]
    file_name = f"/test_writing_csv_file_{x}.csv"
    full_path = f"{path}{file_name}"
    writing_files.write_csv_file(full_path, headers, content)
    response = reading_files.reading_csv_file(full_path)
    combine = list()
    combine.append(headers)
    for row in content:
        combine.append(row)
    assert response
    assert response == combine
