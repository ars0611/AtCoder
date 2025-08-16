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
m = int(input())
a = []
while m > 0:
    for i in range(10,-1,-1):
        if m // 3**i > 0:
            a_i = i
            m -= 3**a_i
            break
    a.append(a_i)

print(len(a))
print(*a)