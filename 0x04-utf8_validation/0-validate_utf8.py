#!/usr/bin/python3
"""UTF-8 Validation"""

# data = [229, 65, 127, 256]
# print([bin(ch)[2:].zfill(8) for ch in data])
# data = [80, 121, 116, 104, 111, 110, 32, 105, 115, 32, 99, 111, 111, 108, 33]
# print([bin(ch)[2:].zfill(8) for ch in data])


def check_one_byte(data, index):
    """ checks one byte of data if it is a valid utf-8 """

    try:
        if data[index].startswith('0'):
            return (True, index + 1)
    except IndexError:
        pass
    return (False, )


def check_two_bytes(data, index):
    """ checks two bytes of data if it is a valid utf-8 """

    try:
        if data[index].startswith('110'):
            return check_one_byte(data, index + 1)
    except IndexError:
        pass
    return (False, )


def check_three_bytes(data, index):
    """ checks 3 bytes of data if it is a valid utf-8 """

    try:
        if data[index].startswith('1110'):
            return check_two_bytes(data, index + 1)
    except IndexError:
        pass
    return (False, )


def check_four_bytes(data, index):
    """ checks 4 bytes of data if is a valid utf-8 """

    try:
        if data[index].startswith('11110'):
            return check_three_bytes(data, index + 1)
    except IndexError:
        pass
    return (False, )


def check_data(data, index):
    """ checks a data if it as valid utf-8 """

    dt = {
        '0': check_one_byte,
        '110': check_two_bytes,
        '1110': check_three_bytes,
        '11110': check_four_bytes
    }

    for dta, function in dt.items():
        if data[index].startswith(dta):
            return function(data, index)

    return (False, )


def validUTF8(bin_data):
    """ checks a data if it is valid utf-8 """

    if len(bin_data) == 0:
        return

    i = ('', 0)
    # bin_data = [bin(ch)[2:].zfill(8) for ch in data]
    while True:
        i = check_data(bin_data, i[1])
        if not i[0]:
            return False
        elif i[1] >= len(bin_data):
            return True
