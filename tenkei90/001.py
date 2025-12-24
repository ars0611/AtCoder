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
n, l = map(int, input().split())
k = int(input())
a = [0] + list(map(int, input().split())) + [l]

left = 0
right = l
while left < right:
    mid =(left + right) // 2
    cnt = 0
    curEdge = 0
    for i in range(1, n + 1):
        if a[i] - a[curEdge] >= mid:
            cnt += 1
            curEdge = i
        if cnt == k: break
    if cnt >= k and l - a[curEdge] >= mid:
        left = mid + 1
    else:
        right = mid
print(left - 1)

# 長さmid以上のようかんをk個作れるかで二分探索
