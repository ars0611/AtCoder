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
from functools import lru_cache
from functools import cmp_to_key
#----------------------------------------#
def delBrk(s):
    stack = []
    for ch in s:
        stack.append(ch)
        if len(stack) >= 4 and ''.join(stack[-4:]) == '(xx)':
            for _ in range(4):
                stack.pop()
            for _ in range(2):
                stack.append('x')
    return ''.join(stack)

t = int(input())
for _ in range(t):
    a = input().strip()
    b = input().strip()
    print("Yes" if delBrk(a) == delBrk(b) else "No")
