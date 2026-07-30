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
from functools import cmp_to_key
#----------------------------------------#
def compArr(s, t):
    m = len(s)
    for i in range(m):
        if s[i] == t[i]: continue
        return s[i] < t[i]

n = int(input())
p = list(map(int, input().split()))
q = list(map(int, input().split()))
ans = 0
for arr in itertools.permutations(range(1,n + 1), n):
    if compArr(p, arr) and compArr(arr, q):
        ans += 1
print(ans)
