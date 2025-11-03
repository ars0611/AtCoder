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
# ユークリッドの互除法による最大公約数の求値
def Euclidean_GCD(a, b):
    x = max(a, b)
    y = min(a, b)
    while y > 0:
        tmp = x % y
        x = y
        y = tmp
    return x

a, b = map(int, input().split())
gcd = Euclidean_GCD(a, b)
lcm = (a * b) // gcd
print(lcm)