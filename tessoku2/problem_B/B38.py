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
n = int(input())
s = input().strip()

a = [0] * n
a[0] = 1
streak = 1
for i in range(n - 1):
    if s[i] == "A":
        streak += 1
    else:
        streak = 1
    a[i + 1] = streak

b = [0] * n
b[n - 1] = 1
streak = 1
for i in range(n - 2, -1, -1):
    if s[i] == "B":
        streak += 1
    else:
        streak = 1
    b[i] = streak

ans = 0
for i in range(n):
    ans += max(a[i], b[i])
print(ans)

# a基準で最小値、b基準で最小値を決めて、最小値のmaxがその草の最小値