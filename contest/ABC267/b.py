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
s = input().strip()
if s[0] == "1":
    print("No")
else:
    e = set()
    if s[6] == "0":
        e.add(1)
    if s[3] == "0":
        e.add(2)
    if s[1] == s[7] == "0":
        e.add(3)
    if s[4] == "0":
        e.add(4)
    if s[2] == s[8] == "0":
        e.add(5)
    if s[5] == "0":
        e.add(6)
    if s[9] == "0":
        e.add(7)
    for i in range(5):
        if i + 1 in e: continue
        for j in range(i + 1, 6):
            if j + 1 in e:
                for k in range(j + 1, 7):
                    if k + 1 not in e:
                        print("Yes")
                        exit()
    print("No")
