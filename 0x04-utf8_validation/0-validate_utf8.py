#!/usr/bin/python3
"""UTF-8 Validation"""


def check_next_bytes(data, index, n):
    """ checks next n bytes of data if it is a valid utf-8 """

    for i in range(index, index + n):
        try:
            if not data[i].startswith('10'):
                return (False, )
        except IndexError:
            return (False, )
    return (True, i + 1)


def check_data(data, index):
    """ checks a data if it as valid utf-8 """

    if data[index].startswith('0'):
        return (True, index + 1)

    dt = {
        '110': 1,
        '1110': 2,
        '11110': 3
    }

    for dta, next_bytes in dt.items():
        if data[index].startswith(dta):
            return check_next_bytes(data, index + 1, next_bytes)

    return (False, )


def validUTF8(data):
    """ checks a data if it is valid utf-8 """

    if len(data) == 0:
        return True

    i = ('', 0)
    bin_data = []
    try:
        for ch in data:
            if ch < 0 or ch > 1114111:
                return False
            bin_data.append(bin(ch)[2:].zfill(8))
    except TypeError:
        return False

    while True:
        i = check_data(bin_data, i[1])
        if not i[0]:
            return False
        elif i[1] >= len(bin_data):
            return True
