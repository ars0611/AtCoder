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
n = int(input())
a = sorted(list(map(int, input().split())))
b = sorted(list(map(int, input().split())))
d = [abs(a[i] - b[i]) for i in range(n)]
print(sum(d))

# sortして貪欲
# ある二人の通う学校への直線が交差する場合、swapすると不便さの和が小さくなることから、交差させないように通わせるのが最適で、それをsortして左から割り当てることでやれる
