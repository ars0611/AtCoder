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
s = input().strip()
stack = []
for ch in s:
    stack.append(ch)
    if len(stack) >= 3 and stack[-3:] == ["A", "B", "C"]:
        for _ in range(3):
            stack.pop()
print("".join(stack))