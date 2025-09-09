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
a = list(map(int, input().split()))
sl = [a[0]]*n
sr = [a[-1]]*n
for i in range(1, n):
    sl[i] = max(a[i], sl[i-1])
    sr[-i-1] = max(a[-i-1], sr[-i])
d = int(input())
for _ in range(d):
    l, r = map(int, input().split())
    l -= 1
    r -= 1
    print(max(sl[l-1], sr[r+1]))