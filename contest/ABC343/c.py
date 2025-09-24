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
ans = 0
num = 0
while num**3 <= n:
    s = str(num**3)
    rs = s[-1:-len(s)-1:-1]
    if s == rs:
        ans = num ** 3
    num += 1
print(ans)
