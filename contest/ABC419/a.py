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
s = input()
if s == "red":
    print("SSS")
elif s == "blue":
    print("FFF")
elif s == "green":
    print("MMM")
else:
    print("Unknown")