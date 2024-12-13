#!/usr/bin/env python3

import re

from functools import cmp_to_key
from pathlib import Path

def main():

    rules_txt, updates_txt = Path('data.txt').read_text().strip().split("\n\n")
    rules = {tuple(numbers) for numbers in re.findall(r"(\d+)\|(\d+)", rules_txt)}
    updates = [re.findall(r"\d+", update) for update in updates_txt.split("\n")]

    changed_medians_sum = 0
    for update in updates:
        fixed = sorted(update, key=cmp_to_key(lambda x, y: 1 if (y, x) in rules else -1))
        if fixed != update:
            changed_medians_sum += int(fixed[len(fixed) // 2])

    print(f"The sum is : {changed_medians_sum}")

    return 0

if __name__ == '__main__':
    main()