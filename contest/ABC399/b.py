import sys
sys.setrecursionlimit(10*6)
if len(sys.argv) == 2:
    sys.stdin = open(sys.argv[1])
import math
from collections import deque
import bisect

#----------------------------------------#
n = int(input())
p = list(map(int, input().split()))

#人iについて、iの順位はp[i]より高い得点の人数+1
for i in range(n):
    rank = 1
    for j in range(n):
        if p[i] < p[j]:
            rank += 1
    print(rank)