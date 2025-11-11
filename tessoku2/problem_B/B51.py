import sys
if len(sys.argv) == 2:
    sys.stdin = open(sys.argv[1])
sys.setrecursionlimit(10**7)
input = sys.stdin.readline
#----------------------------------------#
import math
import bisect
import itertools
import heapq
from collections import deque
from collections import Counter
from collections import defaultdict
from sortedcontainers import SortedList
from sortedcontainers import SortedSet
from sortedcontainers import SortedDict
from more_itertools import distinct_permutations
#----------------------------------------#
s = input().strip()
idx_stack = list()
brk_stack = list()
for i in range(len(s)):
    if brk_stack and brk_stack[-1] + s[i] == "()":
        brk_stack.pop()
        print(idx_stack.pop() + 1, i + 1)
    else:
        brk_stack.append(s[i])
        idx_stack.append(i)