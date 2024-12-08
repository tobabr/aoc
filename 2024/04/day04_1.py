#!/usr/bin/env python3

from textwrap import wrap

from sympy import false


def find_xmas_normal(x, matrix) -> int:
    return int(''.join(matrix[x:x+4]) == 'XMAS')


def find_xmas_reverse(x, matrix) -> int:
    return int(''.join(matrix[x-3:x+1]) == 'SAMX')


def find_xmas_up(x, y, matrix) -> int:
   return int(''.join([matrix[x-i][y] for i in range(0,4)]) == 'XMAS')


def find_xmas_down(x, y, matrix) -> int:
    return int(''.join([matrix[x+i][y] for i in range(0,4)]) == 'XMAS')


def find_xmas_diag_ld(x, y, matrix) -> int:
    return int(''.join([matrix[x+i][y-i] for i in range(0,4)]) == 'XMAS')


def find_xmas_diag_lu(x, y, matrix) -> int:
    return int(''.join([matrix[x-i][y-i] for i in range(0,4)]) == 'XMAS')


def find_xmas_diag_ru(x, y, matrix) -> int:
    return int(''.join([matrix[x-i][y+i] for i in range(0,4)]) == 'XMAS')


def find_xmas_diag_rd(x, y, matrix) -> int:
    return int(''.join([matrix[x+i][y+i] for i in range(0,4)]) == 'XMAS')

def main():
    word_matrix: list[list] = []

    with open('data.txt', 'r') as f:
        for line in f.readlines():
            word_matrix.append(wrap(line, 1))

    rows = len(word_matrix)
    cols = len(word_matrix[0])
    num_xmas = 0

    for row in range(rows):
        for col in range(cols):
            if not word_matrix[row][col] == 'X':
                continue
            if cols-col > 3:
                num_xmas += find_xmas_normal(col, word_matrix[row])
            if col > 2:
                num_xmas += find_xmas_reverse(col, word_matrix[row])
            if row > 2:
                num_xmas += find_xmas_up(row, col, word_matrix)
            if rows-row > 3:
                num_xmas += find_xmas_down(row, col, word_matrix)
            if row > 2 and cols-col > 3:
                num_xmas += find_xmas_diag_ru(row, col, word_matrix)
            if rows-row > 3 and cols-col > 3:
                num_xmas += find_xmas_diag_rd(row, col,word_matrix)
            if  col > 2 and row > 2:
                num_xmas += find_xmas_diag_lu(row, col, word_matrix)
            if rows-row > 3 and col > 2:
                num_xmas += find_xmas_diag_ld(row, col, word_matrix)

    print(f"Found {num_xmas} XMAS")
    return 0


if __name__ == '__main__':
    main()