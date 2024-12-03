#!/usr/bin/env python3

import re

def mul(val1: int, val2: int) -> int:
    return int(val1)*int(val2)

def main():

    with open('data.txt', 'r') as f:
         data = f.read()

    valid_sections = []
    for s in re.split("do\(\)", data):
        valid_sections.append(re.split("don't\(\)", s)[0])

    sum_total = 0
    for section in valid_sections:
        sum_total += sum([eval(m) for m in re.findall("mul\([0-9]+,[0-9]+\)", section)])

    print(sum_total)
    return 0

if __name__ == '__main__':
    main()