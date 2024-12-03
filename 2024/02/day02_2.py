#!/usr/bin/env python3

def generate_alternate_levels(level: list) -> list[list]:
    alternate_levels = []
    for idx in range(len(level)):
        lcpy = level[:]
        lcpy.remove(level[idx])
        alternate_levels.append(lcpy)
    alternate_levels.insert(0, level)
    return alternate_levels

def valid_decent(level: list) -> bool:
    return any([all(map(lambda x,y: x > y and (0 < abs(x - y) <= 3), lvl, lvl[1:])) for lvl in generate_alternate_levels(level)])

def valid_ascent(level: list) -> bool:
    return any([all(map(lambda x,y: x < y and (0 < abs(x - y) <= 3), lvl, lvl[1:])) for lvl in generate_alternate_levels(level)])

def main():
    levels = []

    with open('data.txt', 'r') as f:
        for line in f.readlines():
            levels.append([int(v) for v in line.split()])

    print(sum([valid_ascent(level) or valid_decent(level) for level in levels]))

    return 0

if __name__ == '__main__':
    main()