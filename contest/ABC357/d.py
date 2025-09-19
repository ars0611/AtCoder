import sys
sys.setrecursionlimit(10**7)
if len(sys.argv) == 2:
    sys.stdin = open(sys.argv[1])
input = sys.stdin.readline
from collections import Counter, deque, defaultdict
from sortedcontainers import SortedSet, SortedList, SortedDict
from more_itertools import distinct_permutations
import heapq, bisect, math, itertools

#----------------------------------------#
n = int(input())
mod = 998244353

k = len(str(n)) # nの桁数
ten_kpower = pow(10, k, mod)
bunshi = n * (pow(ten_kpower, n, mod) - 1) % mod
bunbo = pow(ten_kpower - 1, mod-2, mod) #逆元

ans = bunbo * bunshi % mod
print(ans)