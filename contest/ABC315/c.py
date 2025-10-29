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
n = int(input())
ice = []
for _ in range(n):
    f, s = map(int, input().split())
    ice.append((s, f))
ice.sort()

if ice[-1][1] != ice[-2][1]:
    ans = ice[-1][0] + ice[-2][0]
else:
    ans = max(ice[-1][0], ice[-2][0]) + min(ice[-1][0], ice[-2][0]) // 2
    for i in range(2,n + 1):
        if ice[-i][1] != ice[-1][1]:
            ans = max(ans, ice[-1][0] + ice[-i][0])
print(ans)

# きたねえつぎはぎコード