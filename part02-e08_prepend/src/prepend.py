#!/usr/bin/env python3

class Prepend(object):
    # Add the methods of the class here
    def __init__(self, start):
        self.start = start 
    
    def write(self, param1):
        print(f"{self.start}{param1}")


def main():
    pass
    p = Prepend("+++ ")
    p.write("Hello");

if __name__ == "__main__":
    main()
