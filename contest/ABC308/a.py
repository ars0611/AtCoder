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
s = list(map(int, input().split()))
sorted_s = sorted(s)
for i in range(8):
    if s[i] % 25 != 0:
        print("No")
        break
else:
    if s == sorted_s and 100 <= s[0] and s[7] <= 675:
        print("Yes")
    else:
        print("No")