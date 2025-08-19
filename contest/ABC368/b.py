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
n = int(input())
a = list(map(int, input().split()))
a.sort(reverse = True)
cnt = 0
while a[1] > 0:
    a[0] -= 1
    a[1] -= 1
    a.sort(reverse = True)
    cnt += 1

print(cnt)