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
s, t = input().split()
for w in range(1,len(s)):
    for c in range(w):
        a = ""
        for i in range(c, len(s), w):
                a += s[i]
        if a == t:
            print("Yes")
            exit()
print("No")
