from textwrap import wrap

def find_mas(x, y, matrix) -> int:
    directions = [''.join([matrix[y + i][x+i] for i in range(-1, 2)]),
                  ''.join([matrix[y + i][x-i] for i in range(-1, 2)])]
    return int(all([direction in ('MAS', 'SAM') for direction in directions]))


def main():
    word_matrix: list[list] = []

    with open('data.txt', 'r') as f:
        for line in f.readlines():
            word_matrix.append(wrap(line, 1))

    rows = len(word_matrix)
    cols = len(word_matrix[0])
    num_xmas = 0

    for row in range(1,rows-1):
        for col in range(1,cols-1):
            if not word_matrix[row][col] == 'A':
                continue
            num_xmas += find_mas(col, row, word_matrix)

    print(f"Found {num_xmas} XMAS")
    return 0


if __name__ == '__main__':
    main()
