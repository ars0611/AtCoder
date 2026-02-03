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
w = int(input())
a = []
for i in range(1, 101):
    for j in range(3):
        a.append(100 ** j * i)
print(len(a))
print(*a)

# n進数で3桁で1~wを表すことを考える
# n進数3桁で表せる数の最大値は
# (n - 1) * n**2 + (n - 1) * n + (n - 1) = n**3 - 1
# これ以下の数字は表せるので、n**3 - 1>= 10**6 を満たすnは、n = 101
# 101進数の3桁全部の数字を用意してあげればよい
# これがいわゆる構築問題で、ひらめきを要するのでむずい
