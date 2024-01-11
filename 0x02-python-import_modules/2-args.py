#!/usr/bin/python3
import sys
if __name__ == "__main__":
    print(" {}".format(len(sys.argv) - 1), "arguments.")
    if len(sys.argv) > 1:
        print(":")
        for i in range(1, len(sys.argv)):
            print("{}:{}".format(i, sys.argv[i]))
        else:
            print(".")
