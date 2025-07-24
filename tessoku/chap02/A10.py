import sys
sys.setrecursionlimit(10*6)
if len(sys.argv) == 2:
    sys.stdin = open(sys.argv[1])
import math
from collections import deque
import bisect

#----------------------------------------#
n = int(input())
a = list(map(int, input().split()))
d = int(input())

for _ in range(d):
    l, r = map(int, input().split())
    