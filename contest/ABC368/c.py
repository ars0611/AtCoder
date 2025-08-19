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

t = 0
for i in range(n):

    if t % 3 == 1:
        if h[i] >= 2:
            t += 2
            h[i] -= 4
        else:
            t += 1
            h[i] -= 1

    elif t % 3 == 2:
        t += 1
        h[i] -= 3

    if h[i] > 0:
        t += h[i] // 5 * 3
        h[i] %= 5
        if h[i] >= 3:
            t += 3
        else:
            t += h[i]
print(t)

#もっと読みやすくかけたり,簡単に解けたりするんですかね