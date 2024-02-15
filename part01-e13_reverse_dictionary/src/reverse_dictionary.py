#!/usr/bin/env python3

def reverse_dictionary(d):
    result = {}

    for key, value in d.items():
        for i in range(len(value)):           
            if value[i] in result.keys():
                result[value[i]].append(key)
                #print(f"Key '{value[i]}' already exists. Added '{key}' to values list '{value}'")
            else:
                result[value[i]] = [key]
                #print(f"New key '{value[i]}' value '{values}' added")
    return result

def main():
    #pass
    d={'move': ['liikuttaa'], 'hide': ['piilottaa', 'salata'], 'six': ['kuusi'], 'fir': ['kuusi']}
    print(reverse_dictionary(d))


if __name__ == "__main__":
    main()
