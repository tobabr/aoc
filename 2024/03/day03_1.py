#!/usr/bin/env python3

import re

def mul(val1: int, val2: int) -> int:
    return int(val1)*int(val2)

def main():

    with open('data.txt', 'r') as f:
         data = f.read()

    print(sum([eval(m) for m in re.findall("mul\([0-9]+,[0-9]+\)", data)]))

    return 0

if __name__ == '__main__':
    main()