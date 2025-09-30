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
# 入力
h, w, k = map(int, input().split())
grid = [list(input().strip()) for _ in range(h)]

# 累積和げちがんばりパート
ok_rows = [[0] for _ in range(h)]
ok_cols = [[0] for _ in range(w)]
ng_rows = [[0] for _ in range(h)]
ng_cols = [[0] for _ in range(w)]
for i in range(h):
    for j in range(w):
        if grid[i][j] == ".":
            ok_rows[i].append(ok_rows[i][-1] + 1)
            ng_rows[i].append(ng_rows[i][-1])
        elif grid[i][j] == "x":
            ok_rows[i].append(ok_rows[i][-1])
            ng_rows[i].append(ng_rows[i][-1] + 1)
        else:
            ok_rows[i].append(ok_rows[i][-1])
            ng_rows[i].append(ng_rows[i][-1])
for j in range(w):
    for i in range(h):
        if grid[i][j] == ".":
            ok_cols[j].append(ok_cols[j][-1] + 1)
            ng_cols[j].append(ng_cols[j][-1])
        elif grid[i][j] == "x":
            ok_cols[j].append(ok_cols[j][-1])
            ng_cols[j].append(ng_cols[j][-1] + 1)
        else:
            ok_cols[j].append(ok_cols[j][-1])
            ng_cols[j].append(ng_cols[j][-1])

# 累積和をもとに答え求めるパート
ans = float("inf")
for i in range(h):
    for j in range(w - k + 1):
        if ng_rows[i][j + k] - ng_rows[i][j] == 0:
            ans = min(ans,  ok_rows[i][j + k] - ok_rows[i][j])
        

for j in range(w):
    for i in range(h - k + 1):
        if ng_cols[j][i + k] - ng_cols[j][i] == 0:
            ans = min(ans,  ok_cols[j][i + k] - ok_cols[j][i])

# 出力
print(ans if ans != float("inf") else -1)

# 実装辛すぎる