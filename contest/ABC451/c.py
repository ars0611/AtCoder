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
q = int(input())
query = [tuple(map(int, input().split())) for _ in range(q)]
tree = SortedList()
cnt = 0
ans = []
for t, h in query:
    if t == 1:
        tree.add(h)
        cnt += 1
    else:
        while tree and tree[0] <= h:
            tree.pop(0)
            cnt -= 1
    ans.append(str(cnt))
print('\n'.join(ans))
