#!/usr/bin/env python3

import itertools
import re

def calculate(terms: list) -> int:
    def part(first: str, op: str, second: str) -> int:
        if op == '+':
            return int(first) + int(second)
        else:
            return int(first) * int(second)

    sum = part(*terms[:3])
    idx = 3
    while idx < len(terms):
        sum = part(str(sum), *terms[idx:idx+2])
        idx += 2
    return sum


class Equation:
    def __init__(self, line):
        self._result, *self._terms = re.findall("(\d+)", line)
        self._operators = [p for p in itertools.product(['+', '*'], repeat=len(self._terms)-1)]

    @property
    def sum(self):
        return int(self._result)


    def solvable(self) -> bool:
        for op in self._operators:
            calc = []
            for i in zip(self._terms,op):
                calc.extend(i)
            calc.append(self._terms[-1])

            if calculate(calc) == int(self._result):
                return True
        else:
            return False


def main():
    eqs = []

    with open('data.txt', 'r') as f:
        for line in f.readlines():
            eqs.append(Equation(line))

    print(sum(eq.sum for eq in eqs if eq.solvable()))

    return 0

if __name__ == '__main__':
    main()