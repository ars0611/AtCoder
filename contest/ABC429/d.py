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
n, m, c = map(int, input().split())
a = list(map(int, input().split()))

pos = defaultdict(int)
for ai in a:
    pos[ai] += 1
pos_list = sorted(list(pos.keys()))
l = len(pos_list)

s = [0]
for i in range(l * 2):
    s.append(s[-1] + pos[pos_list[i % l]])

ans = 0
if l > 1:
    for i in range(l):
        if i < l - 1:
            cnt = pos_list[i + 1] - pos_list[i]
        else:
            cnt = m - pos_list[i] + pos_list[0]
        idx = bisect.bisect_left(s, c + s[i + 1])
        ans += (s[idx] - s[i + 1]) * cnt
else:
    ans = m * n
print(ans)
