#!/usr/bin/env python3

import re


def file_listing(filename="src/listing.txt"):
    result = []

    with open(filename, "r") as f:

        for line in f:
            chunk = re.search(r'(\s+\d+\s\w+\s+\d+\s\d+\:\d+\s\S+)', line).group()
            items = chunk.replace(':',' ').split()
            finalList =  []
            
            for i in items:
                finalList.append(int(i)) if i.isdigit() else finalList.append(i)
            result.append(tuple(finalList))

    return result

def main():
    pass
    print(file_listing())

if __name__ == "__main__":
    main()
