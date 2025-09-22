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
ch = [0] * 26
for c in s:
    ch[ord(c) - ord("a")] += 1
m = max(ch)
for i in range(26):
    if ch[i] == m:
        print(chr(i + ord("a")))
        break