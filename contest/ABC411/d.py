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
n, q = map(int, input().split())

# クエリ入力
query =[[] for _ in range(q)]
for i in range(q):
    query[i] = list(input().split())

ans = deque()
server = 0
# クエリ逆順取得
for i in range(q-1, -1, -1):
    p = int(query[i][1])
    if query[i][0] == "1":
        if p == server: # これ以前はserverとなってるpの文字列は無関係なので無視
            server = 0
    elif query[i][0] == "2":
        s = query[i][2]
        if p == server: # serverに文字列追加しているのでansにleftappend
            ans.appendleft(s) # 順でansに足すとans = s + ansで計算量爆発なので逆順にして足す
    else:
        if server == 0:
            server = p # serverと一致しているpcに注目

print("".join(ans))

# 愚直に各pcに文字列足していくとMLEとTLEで地獄った
# q回クエリ処理した後のserverの値を求めたい
# 関係ないpcは無視
# 逆順で見よう <-なんでこの発想になったのか教えてー；；
# serverになってるpcに着目