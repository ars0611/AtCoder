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
# 90度から時計回りにソート
def half(p):
    x, y = p
    return 0 if (y > 0 or (y == 0 and x > 0)) else 1
def declinationSort(a, b):
    ha = half(a)
    hb = half(b)
    if ha != hb:
        return ha - hb
    ax, ay = a
    bx, by = b
    return ax * by - ay * bx
keyFunc = cmp_to_key(declinationSort)

n, q = map(int, input().split())
monsters = [(tuple(map(int, input().split()))) for _ in range(n)]
pos = {i:monsters[i] for i in range(n)}
query = [tuple(map(lambda x:int(x) - 1, input().split())) for _ in range(q)]
monsters.sort(key=keyFunc)
zipped = {monsters[0]:1}
preSum = [0, 1]
cur = 1
for i in range(1, n):
    if declinationSort(monsters[i - 1], monsters[i]) == 0:
        preSum[-1] += 1
    else:
        preSum.append(preSum[-1] + 1)
        cur += 1
    zipped[monsters[i]] = cur
ans = []
for a, b in query:
    if declinationSort(pos[a], pos[b]) > 0:
        res = preSum[-1] - preSum[zipped[pos[a]] - 1] + preSum[zipped[pos[b]]]
    else:
        res = preSum[zipped[pos[b]]] - preSum[zipped[pos[a]] - 1]
    ans.append(str(res))
print("\n".join(ans))

# ToDo: 偏角ソートライブラリ化
