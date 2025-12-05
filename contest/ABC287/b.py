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
n, m = map(int, input().split())
s = [input().strip() for _ in range(n)]
t = [input().strip() for _ in range(m)]
ans = 0
for i in range(n):
    for j in range(m):
        if s[i][3:] == t[j]:
            ans += 1
            break
print(ans)
