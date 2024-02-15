#!/usr/bin/env python3


def main():
    pass

    for i in range(1,11):
        for j in range(1,11):
            if j<10:
                print('{:4d}'.format(i*j),end="")
            else:
                print('{:4d}'.format(i*j))

if __name__ == "__main__":
    main()
