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
n, m = map(int, input().split())
price = []
spec = []
func = []
for _ in range(n):
    p, c, *f = map(int, input().split())
    price.append(p)
    spec.append(c)
    func.append(set(f))

cmp = False
for i in range(n):
    for j in range(n):
        if i == j: continue
        if price[i] >= price[j] and func[j].issuperset(func[i]) and (price[i] > price[j] or spec[j] > spec[i] and func[j].issuperset(func[i])):
            cmp = True
            break

print("Yes" if cmp else "No")