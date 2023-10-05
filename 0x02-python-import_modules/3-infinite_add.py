#!/usr/bin/python3

if __name__ == "__main__":
    import sys

    len = len(sys.argv) - 1
    count = 0
    for i in range(len):
        count += int(sys.argv[i + 1])
    print("{}".format(count))
