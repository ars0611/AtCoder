import sys
if len(sys.argv) == 2:
    sys.stdin = open(sys.argv[1])
sys.setrecursionlimit(10**7)
input = sys.stdin.readline
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
n, m = map(int, input().split())
c = list(input().split())
d = list(input().split())
p = list(map(int, input().split()))
price = {d[i]:p[i + 1] for i in range(m)}

colors = set(d)
ans = 0
for dish in c:
    if dish not in colors:
        ans += p[0]
    else:
        ans += price[dish]
print(ans)