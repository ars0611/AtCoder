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
x = input().strip()
s = ['0']
for xi in x:
    s.append(str(int(xi) + int(s[-1])))
d = s[:]
n = len(d)
for i in range(n - 1, 0, -1):
    d[i - 1] = str(int(d[i - 1]) + int(d[i]) // 10)
    d[i] = str(int(d[i]) % 10)
print(int(''.join(d)))

# キャストしすぎて汚い
