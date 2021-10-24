"""The following module demonstrates how to read files"""
import json
import csv


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


def reading_csv_file(file):
    """Reading csv files

    :type file:
    :param file:

    :raises:

    :rtype:
    """

    response = list()
    with open(file, 'r') as csv_file:
        csv_reader = csv.reader(csv_file)
        for row in csv_reader:
            response.append(row)
    return response
