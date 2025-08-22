import sys
sys.setrecursionlimit(10**7)
if len(sys.argv) == 2:
    sys.stdin = open(sys.argv[1])
from collections import Counter, deque, defaultdict
from sortedcontainers import SortedSet, SortedList, SortedDict
import heapq, bisect, math, itertools, copy

#----------------------------------------#
# 入力
n, m, sx, sy = map(int, input().split())
hx = defaultdict(SortedSet) #x座標key上の家のy座標
hy = defaultdict(SortedSet) #y座標key上の家のx座標
for i in range(n):
    x, y = map(int, input().split())
    hx[x].add(y)
    hy[y].add(x)

# 毎回にぶたんで移動前と移動後の間の区間に家があるか調べる
# あるなら,その座標配列で持っといて,あとで削除
# hx,hyどちらでも削除しなといけないことに注意
# 多分TLEの嘘解法
cnt = 0
curx = sx
cury = sy
for i in range(m):
    d, c = input().split()
    c = int(c)
    todel = []
    if d == "U":
        l = hx[curx].bisect_left(cury)
        r = hx[curx].bisect_right(cury + c)
        for y in hx[curx][l:r]:
            if y > cury:
                todel.append((curx,y))
        cury += c
    elif d == "D":
        l = hx[curx].bisect_left(cury - c)
        r = hx[curx].bisect_right(cury)
        for y in hx[curx][l:r]:
            if y < cury:
                todel.append((curx,y))
        cury -= c
    elif d == "L":
        l = hy[cury].bisect_left(curx - c)
        r = hy[cury].bisect_right(curx)
        for x in hy[cury][l:r]:
            if x < curx:
                todel.append((x, cury))
        curx -= c
    elif d == "R":
        l = hy[cury].bisect_left(curx)
        r = hy[cury].bisect_right(curx + c)
        for x in hy[cury][l:r]:
            if x > curx:
                todel.append((x, cury))
        curx += c

    for x, y in todel:
        hx[x].discard(y)
        hy[y].discard(x)
    cnt += len(todel)

print(curx, cury, cnt, end = " ")

# いやこれ通るんかーい
# 消される家の数は高々n個で,移動はm回だからO((m+n)logn)くらいで十分間に合う？