import sys
sys.setrecursionlimit(10**10)
if len(sys.argv) == 2:
    sys.stdin = open(sys.argv[1])
input = sys.stdin.readline
from collections import Counter, deque, defaultdict
from sortedcontainers import SortedSet, SortedList, SortedDict
from more_itertools import distinct_permutations
import heapq, bisect, math, itertools

#----------------------------------------#
def merge(ans, size):
    seen.add(size)
    cnt = slimes[size] // 2
    if cnt != 0:
        slimes[2 * size] += cnt
        return merge(ans - cnt, 2 * size)
    return ans

n = int(input())
slimes = defaultdict(int)

ans = 0
for _ in range(n):
    s, c = map(int, input().split())
    slimes[s] = c
    ans += c

seen = set()
sizes = sorted(list(slimes.keys()))
for size in sizes:
    if size in seen:
        continue
    ans = merge(ans, size)

print(ans)