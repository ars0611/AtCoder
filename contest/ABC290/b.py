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
n, k = map(int, input().split())
s = input().strip()
t = ["x"]*n
cnt = 0
for i in range(n):
    if s[i] == "o":
        t[i] = "o"
        cnt += 1
    if cnt == k: break
print("".join(t))
