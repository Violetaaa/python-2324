#!/usr/bin/env python3

def transform(s1, s2):
    list1 = s1.split()
    list2 = s2.split()

    intList1 = list(map(int, list1))
    intList2 = list(map(int, list2))

    return [x*y for x,y in zip(intList1, intList2)]

#    return [ a*b for (a, b) in zip(map(int, s1.split()), map(int, s2.split())) ]


def main():
    print(transform("1 5 3", "2 6 -1"))


if __name__ == "__main__":
    main()
