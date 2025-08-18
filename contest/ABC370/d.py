import sys
sys.setrecursionlimit(10**7)
if len(sys.argv) == 2:
    sys.stdin = open(sys.argv[1])
from collections import Counter
from collections import deque
from collections import defaultdict
from sortedcontainers import SortedSet, SortedList, SortedDict
import heapq
import bisect
import math
import itertools
import copy

#----------------------------------------#
h, w, q = map(int, input().split())

#なんと実装時間制限4sec
#rows[i],cols[i]でそれぞれi+1行,列について壁を持つマスを順序付き集合で管理してもぎりぎり間に合う？
rows = [SortedSet(range(w)) for _ in range(h)]
cols = [SortedSet(range(h)) for _ in range(w)]

for _ in range(q):
    
    r, c = map(int, input().split())
    r -= 1
    c -= 1
    
    #壁があるときそこだけ破壊
    if c in rows[r]:
        rows[r].discard(c)
        cols[c].discard(r)
        continue

    #破壊予定の壁の座標を格納
    to_del = []
    idx_r = rows[r].bisect_left(c)
    
    #左隣の壁
    if idx_r > 0:
        to_del.append((r, rows[r][idx_r - 1]))
    #右隣の壁
    if idx_r < len(rows[r]):
        to_del.append((r, rows[r][idx_r]))

    idx_c = cols[c].bisect_left(r)
    
    #上隣の壁
    if idx_c > 0:
        to_del.append((cols[c][idx_c - 1], c))
    
    #下隣の壁
    if idx_c < len(cols[c]):
        to_del.append((cols[c][idx_c], c))

    for rr, cc in to_del:
        rows[rr].discard(cc)
        cols[cc].discard(rr)

ans = 0
for i in range(h):
    ans += len(rows[i])
print(ans)

#なんか実行時間1963msですごい。なんで予想より早いのかわからん
#添え字のバグ取りと壁を同時に破壊するのが難しかった