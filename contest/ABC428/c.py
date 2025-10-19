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
q = int(input())
stack = [0]
min_stack = [0]
for _ in range(q):
    query = list(input().split())
    if query[0] == "1":
        stack.append(stack[-1] + 1 if query[1] =="(" else stack[-1] - 1)
        min_stack.append(min(min_stack[-1], stack[-1]))
    else:
        stack.pop()
        min_stack.pop()
    print("Yes" if stack[-1] == min_stack[-1] == 0 else "No")