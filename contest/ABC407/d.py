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
import functools

@functools.cache
def dfs(mask, cur_xor):
    if mask == all_masked:
        return cur_xor
    
    i = 0
    while (mask >> i) & 1:
        i += 1
    r, c = divmod(i, w)

    best = dfs(mask | (1 << i), cur_xor ^ grid[r][c])
    if c + 1 < w and ((mask >> (i + 1) & 1)) == 0:
        best = max(best, dfs(mask | (1 << i) | (1 << (i + 1)), cur_xor))
    if r + 1 < h and ((mask >> (i + w)) & 1) == 0:
        best = max(best, dfs(mask | (1 << i) | (1 << (i + w)), cur_xor))

    return best


h, w = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(h)]
all_masked = (1 << (h * w)) - 1

print(dfs(0, 0))