#!/usr/bin/python3
"""Log parsing"""
import sys
import re


def print_stats(size, status_codes):
    """ prints the statistics """

    print("File size: {}".format(size))
    for key in sorted(status_codes.keys()):
        if status_codes[key] != 0:
            print("{}: {}".format(key, status_codes[key]))


pattern = (
    r'^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}\s-\s\['
    r'\d{2}/[A-Za-z]{3}/\d{4}:\d{2}:\d{2}:\d{2}\s\+\d{4}\]'
    r'\s"GET\s/projects/260\sHTTP/1\.1"\s\d{3}\s\d+$'
)

size = 0
status_codes = {
    '200': 0,
    '301': 0,
    '400': 0,
    '401': 0,
    '403': 0,
    '404': 0,
    '405': 0,
    '500': 0
}
counter = 0

for line in sys.stdin:
    try:
        line = line.strip()
        line = line.split()
        size += int(line[-1])
        try:
            status_codes[line[-2]] += 1
        except KeyError:
            pass
        print(size, status_codes)
        counter += 1
        if counter == 10:
            print_stats(size, status_codes)
            counter = 0
    except KeyboardInterrupt:
        print_stats(size, status_codes)
