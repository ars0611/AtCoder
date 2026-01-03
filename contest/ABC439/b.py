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
from functools import lru_cache
#----------------------------------------#
n = int(input())
calced = set()
ans = "Yes"
def solve(k):
    global ans
    if k in calced:
        ans = "No"
        return
    if k == 1:
        ans = "Yes"
        return
    calced.add(k)
    res = 0
    for num in str(k):
        res += int(num)**2
    solve(res)
solve(n)
print(ans)
