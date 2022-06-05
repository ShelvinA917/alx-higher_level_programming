#!/usr/bin/python3
upper = 0
for i in range(ord('z'), ord('a') - 1, -1):
    print("{}".format(chr(i - upper)), end="")
    upper = 32 if upper == 0 else 0
