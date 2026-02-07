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
n = int(input())
a = sorted(list(map(int, input().split())))
ans = []
l = a[-1]
aa = a[:]
while aa and aa[-1] == l:
    aa.pop()
if len(aa) % 2 == 0:
    for i in range(len(aa) // 2):
        if aa[i] + aa[- 1 - i] != l:break
    else:
        ans.append(l)
l = a[0] + a[-1]
if n % 2 == 0:
    for i in range(n // 2):
        if a[i] + a[- 1 - i] != l: break
    else:
        ans.append(l)
print(*ans)
