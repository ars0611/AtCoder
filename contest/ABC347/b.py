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
StrSet = set()
for i in range(len(s)):
    for j in range(len(s)):
        if i + j + 1 <= len(s):
            StrSet.add(s[i:i + j + 1])
print(len(StrSet))

# /n入っててビビったわ危なすぎる