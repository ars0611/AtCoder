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
a = list(map(int, input().split()))
a = [ai / 1 for ai in a]
a75 = [ai * 5 / 7 for ai in a]
a35 = [ai * 5 / 3 for ai in a]
d75 = defaultdict(list)
d35 = defaultdict(list)
for i in range(n):
    d75[a75[i]].append(i)
    d35[a35[i]].append(i)
ans = 0
for i in range(n):
    if a[i] not in d75.keys() or a[i] not in d35.keys(): continue
    idx75 = bisect.bisect_left(d75[a[i]], i)
    idx35 = bisect.bisect_left(d35[a[i]], i)
    ans += (len(d75[a[i]]) - idx75) * (len(d35[a[i]]) - idx35) + idx75 * idx35
print(ans)
