"""The following module demonstrates how to read files"""
import json


def read_json_file(file_to_read: str) -> dict:
    """Read a json file.

    :type file_to_read:str:
    :param file_to_read:str:

    :raises:

    :rtype: dict
    """
    json_results = dict()

    with open(file_to_read, 'r') as json_file:
        json_results = json.load(json_file)

    return json_results


if __name__ == '__main__':
    result = read_json_file('./json_test_file.json')
    print(result)