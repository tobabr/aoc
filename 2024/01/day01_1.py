#!/usr/bin/env python3


def main():
    list1 = []
    list2 = []

    with open('data.txt', 'r') as f:
        for line in f.readlines():
            v1, v2 = line.split()
            list1.append(int(v1))
            list2.append(int(v2))

    print(sum([abs(v1 - v2) for v1,v2 in zip(sorted(list1), sorted(list2))]))

    return 0

if __name__ == '__main__':
    main()