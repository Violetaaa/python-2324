#!/usr/bin/env python3

def extract_numbers(s):
    result = []
    for item in s.split():
        try:
            result.append(int(item))
        except ValueError:
            try:
                result.append(float(item))
            except ValueError:
                pass

    return result

def main():
    print(extract_numbers("abd 123 1.2 test 13.2 -1"))

if __name__ == "__main__":
    main()
