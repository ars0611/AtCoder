import sys
sys.setrecursionlimit(10*6)
if len(sys.argv) == 2:
    sys.stdin = open(sys.argv[1])
import math
from collections import deque
import bisect

#--------------------��--------------------#
s = int(input())
if 200 <= s <= 299:
    print("Success")
else:
    print("Failure")