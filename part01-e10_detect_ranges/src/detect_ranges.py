#!/usr/bin/env python3

def detect_ranges(L):
    sortedL = sorted(L)
    rangeStart = 0
    rangeEnd = 0
    listWithRanges = []
    i = 0

    while i < len(sortedL):
        if i + 1 == len(sortedL):
            listWithRanges.append(sortedL[i])
            break
        elif sortedL[i] == sortedL[i+1]-1:
            rangeStart = sortedL[i]
            if i + 2 == len(sortedL):
                rangeEnd = sortedL[i+1]+1
                listWithRanges.append((rangeStart, rangeEnd))
                break
            else:
                i += 1
                while sortedL[i] == sortedL[i+1]-1:
                    if i + 2 == len(sortedL):
                        rangeEnd = sortedL[i+1]+1
                        listWithRanges.append((rangeStart, rangeEnd))
                        i += 1
                        break
                    i += 1     
            if rangeEnd != None and rangeEnd == sortedL[i]+1:
                break
            rangeEnd = sortedL[i]+1
            listWithRanges.append((rangeStart, rangeEnd))
            i += 1
        else:
            listWithRanges.append(sortedL[i])
            i += 1
    return listWithRanges

def main():
    L = [2, 5, 4, 8, 12, 6, 7, 10, 13]
    #L = [-2, 0, 1, 2, 3]
    result = detect_ranges(L)

    print(L)
    print(result)

if __name__ == "__main__":
    main()
