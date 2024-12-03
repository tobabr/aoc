#!/usr/bin/env python3

def valid_decent(level: list) -> bool:
    return all(map(lambda x,y: x > y and (0 < abs(x - y) <= 3), level, level[1:]))

def valid_ascent(level: list) -> bool:
    return all(map(lambda x,y: x < y and (0 < abs(x - y) <= 3), level, level[1:]))

def main():
    levels = []

    with open('data.txt', 'r') as f:
        for line in f.readlines():
            levels.append([int(v) for v in line.split()])

    print(sum([valid_ascent(level) or valid_decent(level) for level in levels]))

    return 0

if __name__ == '__main__':
    main()