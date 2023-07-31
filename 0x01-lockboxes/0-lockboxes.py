#!/usr/bin/python3
""" This module contains a function that checks if boxes can be unlocked"""


def canUnlockAll(boxes):
    """
        checks if all boxes can be unlocked
        boxes is a list of lists
    """

    # create a list to hold all the box numbers from box 1
    # box numbers are the box indexes
    # 0 ommited cos the first box (box at index 0) is assumed to be unlocked
    box_numbers = list(range(1, len(boxes)))

    # loop through box_numbers. Each number represents key to unlock the box
    for key in box_numbers:
        found_key = False  # Key not found initially
        for index, box in enumerate(boxes):
            # skip the box at index being the key value
            # A box can only hold keys to other boxes and not itself
            if index == key:
                continue
            if key in box:  # if the key is contained in a box, key is found
                found_key = True
                break   # No need continuing with loop as key is already found

        # if internal loop finishes with key not found
        if not found_key:
            return False

    # If loop finishes without returning false
    # Means all keys was found
    return True
