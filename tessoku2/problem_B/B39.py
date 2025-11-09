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
n, d = map(int, input().split())
jobs = sorted(list(tuple(map(int, input().split())) for _ in range(n)))

can_order = SortedList()
today = 1
money = 0
for x, y in jobs:
    if today == x:
        can_order.add(y)
    else:
        while today != x:
            if can_order:
                money += can_order.pop()
            today += 1
        can_order.add(y)

while can_order and today != d + 1:
    money += can_order.pop()
    today += 1

print(money)