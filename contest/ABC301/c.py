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
s = (list(input().strip()))
t = (list(input().strip()))

sc = Counter(s)
tc = Counter(t)
atcoder = set(["a", "t", "c", "o", "d", "e", "r"])
for ch in "qazwsxedcrfvtgbyhnujmikolp":
    # 問答無用で不可
    if sc[ch] != tc[ch] and ch not in atcoder:
        print("No")
        break
    
    if sc[ch] > tc[ch] and ch in atcoder:
        tc["@"] -= sc[ch] - tc[ch]
    elif ch in atcoder:
        sc["@"] -= tc[ch] - sc[ch]
else:
    if sc["@"] == tc["@"] and sc["@"] >= 0 and tc["@"] >= 0:
        print("Yes")
    else:
        print("No")