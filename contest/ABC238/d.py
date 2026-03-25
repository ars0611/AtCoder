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
t = int(input())
case = [tuple(map(int, input().split())) for _ in range(t)]
ans = []
for a, s in case:
    if s - 2 * a < 0:
        ans.append("No")
        continue
    if (s - 2 * a) & a > 0:
        ans.append("No")
    else:
        ans.append("Yes")
print('\n'.join(ans))
# aで立ってるビットはx, yどっちもたってる
# sを作るのに必要なのは立ってるビットを除いた分で、それはs - 2 * a
# s - 2 * aとaのandが0でないといけないと思う
