#!/usr/bin/env python3

def triple(a):
    return a*3
def square(b):
    return b**2
def main():
    pass
    for i in range(1,11):
        tripleRes=triple(i)
        squareRes=square(i)
        if squareRes > tripleRes:
            break
        print(f"triple({i})=={tripleRes} square({i})=={squareRes}")


if __name__ == "__main__":
    main()
