import sys
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
if len(sys.argv) == 2:
    sys.stdin = open(sys.argv[1])
#----------------------------------------#
n, d = map(int, input().split())
s = [input().strip() for _ in range(n)]
ans = 0
for i in range(d):
    for j in range(i, d):
        for sk in s:
            if sk[i:j + 1] != "o"*(j - i + 1):
                break
        else:
            ans = max(ans, j - i + 1)
print(ans)