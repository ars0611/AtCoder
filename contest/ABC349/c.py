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
s = input().strip()
t = input().strip()
t = t.lower()

cnt = 0
for i in range(len(s)):
    if s[i] == t[cnt]:
        cnt += 1
    if cnt == 3:
        break

if cnt == 3 or cnt == 2 and t[2] == "x":
    print("Yes")
else:
    print("No")