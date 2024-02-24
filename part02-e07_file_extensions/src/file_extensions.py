#!/usr/bin/env python3
import re

def file_extensions(filename):
    pattern = r'\.([^.\/\\]+)$'
    extensions = {}
    noExtension = []
    with open(filename, "r") as f:
        for l in f:
            line = l.strip()
            foundExt = re.search(pattern, line)
            if foundExt:
                cleanedFoundExt = foundExt.group().strip(".")
                if cleanedFoundExt in extensions:
                    ExistentExt = extensions[cleanedFoundExt]
                    ExistentExt.append(line)
                    extensions[cleanedFoundExt] = ExistentExt
                else:
                    extensions[cleanedFoundExt] = [line]
            else:
                noExtension.append(line)

    return (noExtension, extensions)

def main():
    pass
    noExtension, extensions = file_extensions('src/filenames.txt')
    
    print(f"{len(noExtension)} files with no extension")
    for key, value in extensions.items():
        print(f"{key} {len(value)}")

if __name__ == "__main__":
    main()
