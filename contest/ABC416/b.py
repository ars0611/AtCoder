import sys
sys.setrecursionlimit(10*6)
if len(sys.argv) == 2:
    sys.stdin = open(sys.argv[1])
import math
from collections import deque
import bisect

#----------------------------------------#
s = input()
l_s =[]
t = ["."]*(len(s))

for i in range(len(s)):
    l_s.append(s[i])
    if s[i] == "#":
        t[i] = "#"

flag = True
for i, v in enumerate(l_s):
    if flag and v == "#" and i-1 >= 0 and t[i-1] != "#":
        t[i-1] = "o"
        flag = False
    if not flag and v == "#":
        flag = True
    if flag and i == len(s)-1 and v != "#":
        t[i] = "o"

print("".join(t))
