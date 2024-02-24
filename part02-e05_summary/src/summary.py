#!/usr/bin/env python3

import statistics
import sys
import re

def summary(filename):
    numList = []
    with open(filename, "r") as f:
        for num in f:
            if isAdigit(num):
                numList.append(float(num))
    
    getSum = sum(numList)
    getAverage = sum(numList) / len(numList)
    getStandardDeviation = statistics.stdev(numList)

    return (getSum, getAverage, getStandardDeviation)

def isAdigit(text, pat=r'^-*\d+\.*\d*[ \t]*$'):
    if re.search(pat, text) != None:
        return True
    return False

def main():
    pass
    for i in range(1, len(sys.argv)):
        result = summary(sys.argv[i])
        print(f"File: {sys.argv[i]} Sum: {result[0]:.6f} Average: {result[1]:.6f} Stddev: {result[2]:.6f}" )

if __name__ == "__main__":
    main()
