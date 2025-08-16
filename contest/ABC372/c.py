import sys
sys.setrecursionlimit(10**7)
if len(sys.argv) == 2:
    sys.stdin = open(sys.argv[1])
from collections import Counter
from collections import deque
from collections import defaultdict
from sortedcontainers import SortedSet, SortedList, SortedDict
import heapq
import bisect
import math
import itertools
import copy

#----------------------------------------#
n, q = map(int, input().split())
s = list(input())
ans = 0
for i in range(n-2):
    if s[i] == "A" and s[i+1] == "B" and s[i+2] == "C":
        ans += 1
for _ in range(q):
    x, c = input().split()
    x = int(x) - 1
    if s[x-2:x+1] == ["A", "B", "C"] or s[x-1:x+2] == ["A", "B", "C"] or s[x:x+3] == ["A", "B", "C"]:
        ans -= 1
    s[x] = c
    if s[x-2:x+1] == ["A", "B", "C"] or s[x-1:x+2] == ["A", "B", "C"] or s[x:x+3] == ["A", "B", "C"]:
        ans += 1
    print(ans)
