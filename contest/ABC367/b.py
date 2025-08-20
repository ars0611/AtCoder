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
x = float(input())
x = int(x * 1000)
comp = True
if x == 0:
    print(0)
    exit()
i = 0
cnt = 0
while comp and i < 3:
    if x % 10 == 0:
        x //= 10
        cnt += 1
    else:
        comp = False
    i += 1
if cnt == 3:
    print(x//10**(3-cnt))
else:
    print(x/10**(3-cnt))