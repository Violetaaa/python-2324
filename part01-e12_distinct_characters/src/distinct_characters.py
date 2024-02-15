#!/usr/bin/env python3

def distinct_characters(L):
    dict = {}
    for word in L:
        dict[word] = len(set(word))
    return dict

def main():
    print(distinct_characters(["check", "look", "try", "pop"]))

if __name__ == "__main__":
    main()
