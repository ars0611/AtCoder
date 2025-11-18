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

lb = 0
rb = 0
for i in range(len(s)):
    if s[i] != "B": continue
    if lb == 0:
        lb = i + 1
    else:
        rb = i + 1
term1 = lb % 2 != rb % 2

cmp = False
for i in range(len(s)):
    if s[i] == "R":
        cmp = not cmp
    if cmp and s[i] == "K":
        term2 = True
    elif s[i] == "K":
        term2 = False

print("Yes" if term1 and term2 else "No")