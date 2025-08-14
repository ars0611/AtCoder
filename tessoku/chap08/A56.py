import sys
sys.setrecursionlimit(10**7)
if len(sys.argv) == 2:
    sys.stdin = open(sys.argv[1])
from collections import Counter
from collections import deque
from collections import defaultdict
import heapq
import bisect
import math
import itertools
import copy
from sortedcontainers import SortedSet, SortedList, SortedDict

#----------------------------------------#
n, q = map(int, input().split())
s = input()
for i in range(q):
    a, b, c, d = map(int, input().split())
    if s[a-1:b] == s[c-1:d]:
        print("Yes")
    else:
        print("No")