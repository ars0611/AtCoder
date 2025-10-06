import sys
sys.setrecursionlimit(10**7)
if len(sys.argv) == 2:
    sys.stdin = open(sys.argv[1])
input = sys.stdin.readline
from collections import Counter, deque, defaultdict
from sortedcontainers import SortedSet, SortedList, SortedDict
from more_itertools import distinct_permutations
import heapq, bisect, math, itertools

#----------------------------------------#
a, m, l, r = map(int, input().split())
if l <= a <= r:
    ans = (r - a) // m + (a - l) // m + 1
elif l <= r < a:
    ans = (a - l) // m - (a - r) // m
    if (a - r) % m == 0:
        ans += 1
else:
    ans = (r - a) // m - (l - a) // m
    if (l - a) % m == 0:
        ans += 1
print(ans)

# b問題に茶diffだし場合分け考えるゲームだし数学すぎる。境界の扱いに気を付けようって感じだ