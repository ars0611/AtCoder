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
n,m = map(int, input().split())
c = [False]*n
for i in range(m):
    a,b = input().split()
    a =int(a) - 1
    if c[a] == False and b == "M":
        print("Yes")
        c[a] = True
    else:
        print("No")