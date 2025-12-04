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
a = list(map(int, input().split()))
m = int(input())
b = set(map(int, input().split()))
x = int(input())
stairs = [False]*(x + 1)
stairs[0] = True
for i in range(x + 1):
    if not stairs[i]: continue
    for j in range(n):
        if i + a[j] <= x and i + a[j] not in b:
            stairs[i + a[j]] = True
print("Yes" if stairs[x] else "No")
