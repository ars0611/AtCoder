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
n = input().strip()
p = len(n) - 1

ans = 0
for d in range(len(n)):
    num = int(n[d])
    for k in range(1, 10):
        if k < num:
            ans += k * 10**(p - d) * (int(n) // 10**(p - d + 1) + 1)
        elif k == num:
            ans += k * (10**(p - d) * (int(n) // 10**(p - d + 1)) + (int(n) % 10**(p - d)) + 1)
        else:
            ans += k * 10**(p - d) * (int(n) // 10**(p - d + 1))

print(ans)

# 実験頑張ろう界隈