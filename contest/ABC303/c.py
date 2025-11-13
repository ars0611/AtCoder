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
n, m, h, k = map(int, input().split())
s = input().strip()
item = set()
is_used = dict()
for _ in range(m):
    xi, yi = map(int, input().split())
    key = xi * 2 * 10 ** 5 + yi
    item.add(key)
    is_used[key] = False

x = 0
y = 0
hp = h
move = {"R": (1, 0), "L":(-1, 0), "U":(0, 1), "D":(0, -1)}
for ch in s:
    x += move[ch][0]
    y += move[ch][1]
    hp -= 1
    
    if hp < 0: 
        print("No")
        break

    key = x * 2 * 10 ** 5 + y
    if hp < k and key in item and not is_used[key]:
        hp = k
        is_used[key] = True
else:
    print("Yes")