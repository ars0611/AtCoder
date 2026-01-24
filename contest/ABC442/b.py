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
q = int(input())
sound = 0
songFlg = False
for _ in range(q):
    a = int(input())
    if a == 1:
        sound += 1
    elif a == 2:
        sound = sound - 1 if sound > 0 else sound
    else:
        songFlg = not songFlg
    print("Yes" if sound >= 3 and songFlg else "No")
