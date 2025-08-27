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
s = input()
R_idx = -1
M_idx = -1
for i in range(len(s)):
    if s[i] == "R":
        R_idx = i
    elif s[i] == "M":
        M_idx = i

if R_idx < M_idx:
    print("Yes")
else:
    print("No")