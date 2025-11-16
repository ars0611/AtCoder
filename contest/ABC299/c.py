import sys
if len(sys.argv) == 2:
    sys.stdin = open(sys.argv[1])
sys.setrecursionlimit(10**7)
input = sys.stdin.readline
#----------------------------------------#
import math
import bisect
import itertools
import heapq
from collections import deque
from collections import Counter
from collections import defaultdict
from sortedcontainers import SortedList
from sortedcontainers import SortedSet
from sortedcontainers import SortedDict
from more_itertools import distinct_permutations
#----------------------------------------#
n = int(input())
s = input().strip()

ans = -1
l = 0
r = 0
while l < n:
    while r < n and s[l] == s[r] == "o":
        r += 1
    if r != l:
        ans = max(ans,r - l)
    l = r + 1
    r = l

print(ans if n != ans else -1)