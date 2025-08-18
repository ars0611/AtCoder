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
a, b = map(int, input().split())
if (a - b) % 2 == 0 and a != b:
    print(3)
elif a != b:
    print(2)
else:
    print(1)
