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
s = input().strip()
nums = set(range(10))
flg = len(s) == 8 and s[0].isupper() and s[-1].isupper() and all(int(s[i]) in nums for i in range(1, 7)) and 100000 <= int(s[1:7]) <= 999999
print("Yes" if flg else "No")

