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
n, k = map(int, input().split())
a = list(map(int, input().split()))
a.sort()
ans = float("inf")
for i in range(n-k-1):
    m = a[i]
    ans =min(ans, a[i+n-k-1] - m)
print(ans)

#sortして末項-初項が答え。
#都合よく削除するのは難しい。
#n-kの長さの数列を作ると考える。
#高々k+1個しかないので全探索で間に合う。
#毎回ansと作った数列のmax - minを比較する。