import sys
if len(sys.argv) == 2:
    sys.stdin = open(sys.argv[1])
sys.setrecursionlimit(10**7)
input = sys.stdin.readline
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

def power(a, b, mod):
    # 指数を2進変換した際のビット数を求める。
    k = 0
    while 1 << k <= b:
        k += 1

    # 繰り返し二乗法
    res = 1
    p = a
    for i in range(k):
        if (1 << i) & b:
            res = (res * p) % mod
        p = (p * p) % mod
    
    return res

a, b = map(int, input().split())
print(power(a, b, 1000000007))