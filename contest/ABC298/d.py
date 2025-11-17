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
mod = 998244353
s_mod = 1
digits = [1]
power10 = [1]
for i in range(q):
    power10.append(power10[-1] * 10 % mod)
p = 0
cnt = 0
for _ in range(q):
    query = list(map(int, input().split()))
    if query[0] == 1:
        s_mod *= 10
        s_mod += query[1]
        s_mod %= mod
        p += 1
        digits.append(query[1])
    elif query[0] == 2:
        s_mod -= digits[cnt] * power10[p] % mod
        cnt += 1
        p -= 1
    else:
        s_mod %= mod
        print(s_mod)