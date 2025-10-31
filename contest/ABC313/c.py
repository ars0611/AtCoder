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
a = sorted(list(map(int, input().split())))

aim = sum(a) // n
p = 0
m = 0
for i in range(n):
    if a[i] < aim:
        p += aim - a[i]
    if a[i] > aim:
        m += a[i] - aim - 1

print(max(p, m))

# 勘すぎる。なんでこれで解けるか言語化できなかったけど、通りそうだから提出したら通った。