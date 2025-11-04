import sys
if len(sys.argv) == 2:
    sys.stdin = open(sys.argv[1])
sys.setrecursionlimit(10**7)
input = sys.stdin.readline
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
t = int(input())
for _ in range(t):
    n = int(input())
    s = list(input().strip())
    l = n
    r = n
    for i in range(n - 1):
        if ord(s[i]) > ord(s[i + 1]):
            l = i
            break
    for i in range(l + 1, n):
        if ord(s[l]) < ord(s[i]):
            r = i - 1
            break
    shifted = s[:l] + s[l + 1: r + 1] + s[l:l + 1] + s[r + 1:]
    print("".join(shifted))