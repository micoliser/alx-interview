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


pattern = re.compile(
    r"([0-2]?[0-9]?[0-9]\.[0-2]?[0-9]?[0-9]\.[0-2]?[0-9]?[0-9]\.[0-2]?[0-9]?[0-9])\ \-\ \[([0-9]{4}\-[0-1]{1}[0-9]{1}\-[0-3]{1}[0-9]{1}\ [0-2]{1}[0-9]{1}\:[0-5]{1}[0-9]{1}\:[0-5]{1}[0-9]{1}\.[0-9]{6})\]\ (\"GET\ \/projects\/260\ HTTP\/1\.1\")\ (200|301|400|401|403|404|405|500)\ ([1-9][0-9]*)")

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

try:
    for line in sys.stdin:
        if re.match(pattern, line) is None:
            continue
        line = line.strip()
        line = line.split()
        size += int(line[-1])
        try:
            status_codes[line[-2]] += 1
        except KeyError:
            pass
        counter += 1
        if counter == 10:
            print_stats(size, status_codes)
            counter = 0
except KeyboardInterrupt:
    print_stats(size, status_codes)
    raise
