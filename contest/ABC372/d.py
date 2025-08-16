import sys
sys.setrecursionlimit(10**7)
if len(sys.argv) == 2:
    sys.stdin = open(sys.argv[1])
from collections import Counter
from collections import deque
from collections import defaultdict
from sortedcontainers import SortedSet, SortedList, SortedDict
import heapq
import bisect
import math
import itertools
import copy

#----------------------------------------#
n = int(input())
h = list(map(int, input().split()))

ans = [0]*n
stuck = []
for i in range(n-2, -1, -1):
    while stuck and h[stuck[-1]] < h[i+1]:
        stuck.pop()
    stuck.append(i+1)
    ans[i] = len(stuck)
print(*ans)
#なんでこれでうまくいくのかよくわからない