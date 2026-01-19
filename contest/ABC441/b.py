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
from functools import lru_cache
#----------------------------------------#
n, m = map(int, input().split())
s = set(input().strip())
t = set(input().strip())
q = int(input())
for _ in range(q):
    w = input().strip()
    if all(ch in s and ch in t for ch in w):
        print("Unknown")
    elif all(ch in s for ch in w):
        print("Takahashi")
    else:
        print("Aoki")
