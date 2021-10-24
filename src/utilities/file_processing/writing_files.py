"""The following module demonstrates how to read files"""
import json
import csv


def write_json_file(file_name, json_file_content):
    """Write JSON file.

    :type file_name:
    :param file_name:

    :raises:

    :rtype:
    """
    with open(file_name, 'w') as json_file:
        json.dump(json_file_content, json_file)


def write_csv_file(file_name, headers, csv_file_content):
    """Example of how to write a csv file.

    :type file_name:
    :param file_name:

    :type headers:
    :param headers:

    :type csv_file_content:
    :param csv_file_content:

    :raises:

    :rtype:
    """
    with open(file_name, 'w') as csv_file:
        csv_writer = csv.writer(csv_file)
        csv_writer.writerow(headers)
        csv_writer.writerows(csv_file_content)
