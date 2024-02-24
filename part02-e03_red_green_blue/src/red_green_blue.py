#!/usr/bin/env python3

import re

def red_green_blue(filename="src/rgb.txt"):
    result = []
    with open(filename, "r") as f:
        next(f)
        for line in f:
            fields = re.match(r'^\s*(\d+)\s+(\d+)\s+(\d+)\s+(.+)$', line.strip())
            formattedFields = '\t'.join(fields.groups())    
            result.append(formattedFields)
        return result


def main():
    pass
    print(red_green_blue())
if __name__ == "__main__":
    main()
