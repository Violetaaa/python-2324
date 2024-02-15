#!/usr/bin/env python3

def find_matching(L, pattern):
    matches = []
    for i,element  in enumerate(L):
        if pattern in element:
            matches.append(i)
    return matches

def main():
    print(find_matching(["sensitive", "engine", "rubbish", "comment"], "en"))

if __name__ == "__main__":
    main()
