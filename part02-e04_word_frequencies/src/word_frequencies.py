#!/usr/bin/env python3

def word_frequencies(filename):
    result = {}

    with open(filename, "r") as f:
        for line in f:
            wordList = line.split()
            for w in wordList:
                cleaned = w.strip("""!"#$%&'()*,-./:;?@[]_""")
                if cleaned in result.keys():
                    result[cleaned] += 1
                else:
                    result[cleaned] = 1
    return result

def main():
    pass
    print(word_frequencies("src/alice.txt"))

if __name__ == "__main__":
    main()
