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
idx = []
for i in range(len(s)):
    if s[i] == "|":
        idx.append(i)
print(s[0:idx[0]] + s[idx[1]+1:len(s)])