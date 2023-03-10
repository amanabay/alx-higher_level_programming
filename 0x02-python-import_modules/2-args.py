#!/usr/bin/python3

if __name__ == "__main__":
    import sys

    print(f"{len(sys.argv)} arguments:")
    for i in range(len(sys.argv)):
        print(f"{i + 1}: {sys.argv[i]}")
