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
n, k = map(int, input().split())
ans = [k]
for i in range(n):
    nxt = []
    for a in ans:
        nxt.append(a // 2)
        nxt.append(a - a // 2)
    ans = nxt[:]
u = max(ans) - min(ans)
print(u)
print(*ans)

# あまりにも解説AC
# 数列を構成したいからアンバランスを求めるときの逆順の操作をしたい
# kを均等に配りたい
# アンバランス求めた時の数列は[k]だから普通にn回2で割って配っていくだけ