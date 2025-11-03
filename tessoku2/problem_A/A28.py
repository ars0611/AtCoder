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
num = 0
for _ in range(n):
    t, a = input().split()
    a = int(a)
    if t == "+":
        num += a
    if  t == "-":
        num -= a
    if t == "*":
        num *= a
    num %= 10000
    print(num)