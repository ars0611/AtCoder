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
cmp = False
num = 1
x = 0
while not cmp and num <= n:
    while not cmp and num <= n:
        if num == n:
            cmp = True
        num *= 2
    x += 1
    num = 3 ** x
print("Yes" if cmp else "No")