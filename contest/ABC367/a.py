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
a, b, c = map(int, input().split())
if c <= a <= b or b <= c <= a or a <= b <= c:
    print("Yes")
else:
    print("No")