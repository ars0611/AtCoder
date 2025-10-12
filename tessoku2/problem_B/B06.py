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
s = [0]
for ai in a:
    s.append(s[-1] + ai)
q = int(input())
for _ in range(q):
    l, r = map(int, input().split())
    o = s[r] - s[l-1]
    x = (r - l + 1) - o
    if o > x:
        print("win")
    elif o < x:
        print("lose")
    else:
        print("draw")