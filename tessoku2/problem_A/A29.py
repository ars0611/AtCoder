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
a, b = map(int, input().split())
mod = 1000000007

# print(pow(a, b, mod)) <- これでいいけど繰り返し二乗法で書いてみましょう
k = 0
while 1 << k <= b:
    k += 1

ans = 1
p = a
for i in range(k):
    if (1 << i) & b:
        ans = (ans * p) % mod
    p = (p * p) % mod

print(ans % mod)