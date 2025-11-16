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
q = int(input())
placed = SortedList()
cnt = 0
for _ in range(q):
    t, x = map(int, input().split())
    if t == 1:
        placed.add(x)
        cnt += 1
    else:
        if cnt == 0:
            print(-1)
        else:
            idx = placed.bisect_left(x)
            if idx == cnt:
                print(x - placed[-1])
            elif idx == 0:
                print(placed[idx] - x)
            else:
                print(min(placed[idx] - x, x - placed[idx - 1]))