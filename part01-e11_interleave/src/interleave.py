#!/usr/bin/env python3

def interleave(*lists):
    interleavedList = []
    zippedLists = zip(*lists)
    #print(f"zippedLists: {list(zippedLists)}")

    for l in zippedLists:
        interleavedList.extend(l)
    return interleavedList

def main():
    print(interleave([1, 2, 3], [20, 30, 40], ['a', 'b', 'c']))

if __name__ == "__main__":
    main()
