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
c = [0] * 26
for i in range(len(s)):
    c[ord(s[i]) - ord('a')] += 1

for i in range(1, max(c) + 1):
    if not(c.count(i) == 0 or c.count(i) == 2):
        print("No")
        exit()
print("Yes")