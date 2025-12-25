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
def f(k):
    if k == 0:
        return 1
    if k // 2 in memo.keys() and k // 3 in memo.keys():
        res = memo[k // 2] + memo[k // 3]
        memo[k] = res
    elif k // 2 in memo.keys():
        res = memo[k // 2] + f(k // 3)
    elif k // 3 in memo.keys():
        res = f(k // 2) + memo[k // 3]
    else:
        res = f(k // 2) + f(k // 3)
    return res
memo = {0:1}
n = int(input())
ans = f(n)
print(ans)
# なんかうまくDPしたくなるけどいいや
