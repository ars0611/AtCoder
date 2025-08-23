import sys
sys.setrecursionlimit(10**7)
if len(sys.argv) == 2:
    sys.stdin = open(sys.argv[1])
from collections import Counter, deque, defaultdict
from sortedcontainers import SortedSet, SortedList, SortedDict
import heapq, bisect, math, itertools, copy

#----------------------------------------#
n, q = map(int, input().split())
a = sorted(list(map(int, input().split())))

def check(b, d):
    l = b - d
    r = b + d
    return bisect.bisect_right(a, r) - bisect.bisect_left(a, l)

for i in range(q):
    b, k = map(int, input().split())
    l = 0
    h = 10 ** 9
    while l < h:
        mid = (l + h) // 2
        if check(b, mid) >= k:
            h = mid
        else:
            l = mid + 1
    print(l)

# 答えでにぶたん
# bを中心に,半径dの範囲にあるaの要素の数をcheckで数える
# その数がk以上になる最小のdをにぶたんで求める
# それが答え
# これ,もしかしてようかんパーティーというやつでは？