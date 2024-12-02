#!/usr/bin/env python3


def main():
    list1 = []
    list2 = []

    with open('data.txt', 'r') as f:
        for line in f.readlines():
            v1, v2 = line.split()
            list1.append(int(v1))
            list2.append(int(v2))

    list2.sort()
    multiplier = {}
    index = 0
    times = 1
    while index < len(list2) - 1 :
        if list2[index] != list2[index+1]:
            multiplier[list2[index]] = times
            times = 1
        else:
            times += 1
        index += 1

    print(sum([v*multiplier.get(v, 0) for v in list1]))

    return 0

if __name__ == '__main__':
    main()