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
winNum = 1
drawNum = 0
loseNum = -1
def res(s, t):
    if s == 'G' and t == 'C' or s == 'C' and t == 'P' or s == 'P' and t == 'G':
        return winNum
    elif s == t:
        return drawNum
    else:
        return loseNum

n, m = map(int, input().split())
a = [input().strip() for _ in range(2 * n)]
rank = [(0, i) for i in range(2 * n)]
for i in range(m):
    newRank = []
    for j in range(n):
        pScore, p = rank[2 * j]
        qScore, q = rank[2 * j + 1]
        if res(a[p][i], a[q][i]) == winNum:
            newRank.append((pScore + 1, p))
            newRank.append((qScore, q))
        elif res(a[p][i], a[q][i]) == drawNum:
            newRank.append((pScore, p))
            newRank.append((qScore, q))
        else:
            newRank.append((pScore, p))
            newRank.append((qScore + 1, q))
    newRank.sort(key=lambda x: (-x[0], x[1]))
    rank = newRank[:]
ans = [str(rank[i][1] + 1) for i in range(2 * n)]
print('\n'.join(ans))
