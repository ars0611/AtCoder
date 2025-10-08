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
h, w = map(int, input().split())
grid_a =[list(map(int, input().split())) for _ in range(h)]
grid_b =[list(map(int, input().split())) for _ in range(h)]

# grid_aを行,列それぞれについてこねこねしたやつ
row = list(itertools.permutations(range(h)))
col = list(itertools.permutations(range(w)))

ans = float("inf")
# 順列全探索
for p in row:
    for q in col:
        cmp = True
        # 行の状態p,列の状態qに対し、grid_aのそれぞれのマスがgrid_bと一致しているか
        for i in range(h):
            for j in range(w):
                if grid_b[i][j] != grid_a[p[i]][q[j]]:
                    cmp = False
        # そろった時の処理
        if cmp:
            cnt_p = 0 # pをつくるための操作回数 = 転倒数
            cnt_q = 0
            for k in range(h):
                for l in range(h):
                    if k < l and p[k] > p[l]:
                        cnt_p += 1
            for m in range(w):
                for n in range(w):
                    if m < n and q[m] > q[n]:
                        cnt_q += 1
            ans = min(ans, cnt_p + cnt_q)
print(ans if ans != float("inf") else -1)