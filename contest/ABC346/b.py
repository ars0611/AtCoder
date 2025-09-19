import sys
sys.setrecursionlimit(10**7)
if len(sys.argv) == 2:
    sys.stdin = open(sys.argv[1])
input = sys.stdin.readline
from collections import Counter, deque, defaultdict
from sortedcontainers import SortedSet, SortedList, SortedDict
from more_itertools import distinct_permutations
import heapq, bisect, math, itertools

#----------------------------------------#
w, b = map(int, input().split())
s = "wbwbwwbwbwbw"

for i in range(len(s)):
    cntw = 0
    cntb = 0
    for j in range(w + b):
        if s[(i + j) % len(s)] == "w":
            cntw += 1
        else:
            cntb += 1

    if w == cntw and b == cntb:
        print("Yes")
        exit()
print("No")