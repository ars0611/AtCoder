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
n = int(input())
s = list()
a = list()
m = 10**9 + 1
start = 0
for i in range(n):
    si, ai = input().split()
    ai = int(ai)
    s.append(si)
    a.append(ai)
    if ai <= m:
        start = i
        m = ai

for i in range(start, start + n):
    print(s[i % n])