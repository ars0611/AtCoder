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
s = input().strip()
sa = [0]
sb = [0]
sc = [0]
for ch in s:
    if ch == 'A':
        sa.append(sa[-1] + 1)
        sb.append(sb[-1])
        sc.append(sc[-1])
    elif ch == 'B':
        sa.append(sa[-1])
        sb.append(sb[-1] + 1)
        sc.append(sc[-1])
    else:
        sa.append(sa[-1])
        sb.append(sb[-1])
        sc.append(sc[-1] + 1)
ab = defaultdict(int)
ac = defaultdict(int)
bc = defaultdict(int)
abc = defaultdict(int)
for i in range(n + 1):
    ab[sa[i] - sb[i]] += 1
    ac[sa[i] - sc[i]] += 1
    bc[sb[i] - sc[i]] += 1
    abc[(sa[i] - sb[i], sb[i] - sc[i])] += 1
ans = (n * (n + 1)) // 2
for v in ab.values():
    if v == 1: continue
    ans -= (v * (v - 1)) // 2
for v in ac.values():
    if v == 1: continue
    ans -= (v * (v - 1)) // 2
for v in bc.values():
    if v == 1: continue
    ans -= (v * (v - 1)) // 2
for v in abc.values():
    if v == 1: continue
    ans += (v * (v - 1))
print(ans)
