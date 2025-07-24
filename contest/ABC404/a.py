import sys
sys.setrecursionlimit(10*6)
if len(sys.argv) == 2:
    sys.stdin = open(sys.argv[1])
import math
from collections import deque
import bisect

#----------------------------------------#
S = input()
eng = [(chr(ord("a") + i)) for i in range(26)]
for i in eng:
    if not i in S:
        print(i)
        exit()