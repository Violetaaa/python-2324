#!/usr/bin/env python3

import sys

def file_count(filename):
    lines = 0
    words = 0
    chars = 0
    with open(filename, "r") as f:
        for l in f:
            lines += 1
            words += len(l.split())
            chars += len(l)
    return (lines, words, chars)

def main():
    pass
    for i in range(1, len(sys.argv)):
        result = file_count(sys.argv[i])
        print(f"{result[0]}\t{result[1]}\t{result[2]}\t{sys.argv[i]}")

if __name__ == "__main__":
    main()
