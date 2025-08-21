import sys
sys.setrecursionlimit(10**7)
if len(sys.argv) == 2:
    sys.stdin = open(sys.argv[1])
from collections import Counter, deque, defaultdict
from sortedcontainers import SortedSet, SortedList, SortedDict
import heapq, bisect, math, itertools, copy

#----------------------------------------#
# 入力
n = int(input())
a = [list(map(int, input().split())) for _ in range(n**2)]
s = [[0] * (n+1) for _ in range(n**2+1)]

# 二次元累積和
# 横方向に累積和
for i in range(n**2):
    for j in range(n):
        s[i+1][j+1] = s[i+1][j] + a[i][j]
#縦方向に累積和
for j in range(1, n+1):
    for i in range(1, n**2+1):
        s[i][j] += s[i-1][j]

q = int(input())
# クエリ処理
for _ in range(q):
    lx, rx, ly, ry, lz, rz = map(int, input().split())
    ans = 0
    #xだけうまいことやった
    for i in range(lx, rx+1): 
        ans += s[n*(i-1)+ry][rz] - s[n*(i-1)+ly-1][rz] - s[n*(i-1)+ry][lz-1] + s[n*(i-1)+ly-1][lz-1]
    print(ans)