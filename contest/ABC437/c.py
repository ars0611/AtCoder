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
t = int(input())
for _ in range(t):
    n = int(input())
    deer = [tuple(map(int, input().split())) for _ in range(n)]
    deer.sort(key = lambda x: x[1] + x[0], reverse=True)
    preSumW = [0]
    preSumP = [0]
    for i in range(n):
        preSumW.append(deer[i][0] + preSumW[-1])
        preSumP.append(deer[i][1] + preSumP[-1])
    for i in range(n):
        if preSumP[i + 1] >= preSumW[-1] - preSumW[i + 1]:
            print(n - i - 1)
            break
