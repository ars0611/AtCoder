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
n = int(input())
s = input().strip()
xxx = set()
l = 0
r = 0
while l < n:
    if r < n and s[l] == s[r]:
        xxx.add((ord(s[l]), (r - l + 1)))
        r += 1
    else:
        l = r
print(len(xxx))