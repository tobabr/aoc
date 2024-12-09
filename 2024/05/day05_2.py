#!/usr/bin/env python3


def update_rules(rule: list, ordening_rules: dict) -> None:
    first = ordening_rules.setdefault(rule[0], {'pre': [], 'post': []})
    first['post'].append(rule[1])
    second = ordening_rules.setdefault(rule[1], {'pre': [], 'post': []})
    second['pre'].append(rule[0])

def check_order(idx, update, rule) -> bool:
    #print(f"idx = {idx}, update = {update}, rule = {rule}")
    if idx < len(update)-1  and update[idx+1] not in rule['post']:
        #print(f"{idx} < {len(update)} and {update[idx+1]} not in {rule['post']}")
        return True

    return False

def invalidate_updates(updates: list[list], ordening_rules: dict) -> list[list]:
    invalid_updates = []

    for update in updates:
        if any([check_order(idx, update, ordening_rules.get(number)) for idx, number in enumerate(update)]):
            invalid_updates.append(update)

    return invalid_updates


def main():

    ordening_rules = {}
    updates = []
    with open('data.txt', 'r') as f:
        for line in f:
            line = line.strip()
            if not line:
                break
            update_rules(line.split('|'), ordening_rules)

        for line in f:
            updates.append(line.strip().split(','))

    invalid_updates = invalidate_updates(updates, ordening_rules)
    print(f"Number of valid updates: {len(invalid_updates)}")

    middle_sum = sum([int(update[(len(update)-1)//2]) for update in invalid_updates])
    print(f"The sum is : {middle_sum}")

    return 0

if __name__ == '__main__':
    main()