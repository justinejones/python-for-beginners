"""The following module demonstrates how to read files"""
import json


def write_json_file(file_name, json_file_content):
    """Writes JSON file.

    :type file_name:
    :param file_name:

    :raises:

    :rtype:
    """
    with open(file_name, 'w') as json_file:
        json.dump(json_file_content, json_file)
