#!/usr/bin/python3
""" N Queens puzzle solution program """
import sys


if len(sys.argv) != 2:
    print('Usage: nqueens N')
    sys.exit(1)

try:
    n = int(sys.argv[1])
    if n < 4:
        print('N must be at least 4')
        sys.exit(1)
except ValueError:
    print('N must be a number')
    sys.exit(1)


def check_queen_idx(row, row_num, queens_pos):
    """ """
    for i in range(0, len(row)):
        invalid = False
        if i in queens_pos:
            continue
        for idx, pos in enumerate(queens_pos):
            if pos is None:
                break
            if abs(pos - i) == row_num - idx:
                invalid = True
                break
        if invalid:
            continue
        return i
    return None


def check_possible_placement(row_num, queens_pos, index):
    """ """
    if index in queens_pos:
        return False
    for idx, pos in enumerate(queens_pos):
        if pos is None:
            break
        if abs(pos - index) == row_num - idx:
            return False
    return True


def backtrack(chessboard, queens_pos, current_row_num):
    """ """
    if queens_pos[0] == len(chessboard) - 1:
        return (False, -1)
    prev_row_num = current_row_num - 1
    prev_row = chessboard[prev_row_num]
    prev_row_queen_pos = queens_pos[prev_row_num]
    prev_row[prev_row_queen_pos] = 0

    if prev_row_num == 0:
        prev_row[prev_row_queen_pos + 1] = 'Q'
        queens_pos[prev_row_num] = prev_row_queen_pos + 1
        return (True, prev_row_num)

    for i in range(prev_row_queen_pos + 1, len(prev_row)):
        if check_possible_placement(prev_row_num, queens_pos, i):
            prev_row[i] = 'Q'
            queens_pos[prev_row_num] = i
            return (True, prev_row_num)

    queens_pos[prev_row_num] = None
    return backtrack(chessboard, queens_pos, prev_row_num)


def get_queens_pos(start_idx):
    """ """
    chessboard = [[0 for i in range(n)] for j in range(n)]
    queens_pos = [None for i in range(n)]

    i = 0
    while i < len(chessboard):
        row = chessboard[i]
        if i == 0:
            queen_idx = start_idx
            row[queen_idx] = 'Q'
            queens_pos[0] = queen_idx
            i += 1
            continue
        queen_idx = check_queen_idx(row, i, queens_pos)
        if queen_idx is None:
            done, new_idx = backtrack(chessboard, queens_pos, i)
            if not done:
                return None
            else:
                i = new_idx + 1
                continue
        row[queen_idx] = 'Q'
        queens_pos[i] = queen_idx
        i += 1

    queens_pos_matrx = [[i, queens_pos[i]] for i in range(len(queens_pos))]
    return queens_pos_matrx


idx = 0
while idx < n:
    n_queens_pos = get_queens_pos(idx)
    if n_queens_pos:
        print(n_queens_pos)
        idx = n_queens_pos[0][1] + 1
    else:
        idx += 1
