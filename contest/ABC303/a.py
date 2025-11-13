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
#----------------------------------------#
n = int(input())
s = input().strip()
t = input().strip()

for i in range(n):
    if not(s[i] == t[i] or s[i] + t[i] == "1l" or s[i] + t[i] == "l1" or s[i] + t[i] == "0o" or s[i] + t[i] == "o0"):
        print("No")
        break
else:
    print("Yes")