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
m = set([("(", ")"), ("<", ">"), ("[", "]")])
for i in range(len(s)):
    stack.append(s[i])
    if len(stack) >= 2:
        if (stack[-2], stack[-1]) in m:
            stack.pop()
            stack.pop()
    
print("Yes" if not stack else "No")