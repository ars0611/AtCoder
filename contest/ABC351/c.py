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
a = list(map(int, input().split()))

stack = []
for i in range(n):
    stack.append(a[i])
    while len(stack) > 1 and stack[-1] == stack[-2]:
        size = stack[-1] + 1
        stack.pop()
        stack.pop()
        stack.append(size)

print(len(stack))