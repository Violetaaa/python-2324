#!/usr/bin/env python3

def merge(L1, L2):
    merged = L1 + L2
    
    for i in range (len(merged)):
        for j in range (0, len(merged) - i - 1):
            if merged[j] > merged[j+1]:
                larger = merged[j]
                # swapp
                merged[j] = merged[j+1]
                merged[j+1] = larger
    return merged

def main():
    pass

    L1 = [1,4,7,11,17,23,25]
    L2 = [2,3,8,13,14]

    print(merge(L1,L2))
if __name__ == "__main__":
    main()
