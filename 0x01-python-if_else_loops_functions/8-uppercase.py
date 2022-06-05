#!/usr/bin/python3
def uppercase(str):
    for s in str:
        if ord(s) >= ord('a') and ord(s) <= ord('z'):
            s = chr(ord(s) - 32)
        print("{}".format(s), end="")
    print("")
