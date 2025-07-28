import sys
sys.setrecursionlimit(10**7)
if len(sys.argv) == 2:
    sys.stdin = open(sys.argv[1])
import math
from collections import deque
import bisect
from collections import defaultdict
import itertools

#----------------------------------------#
n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

#まずはdp
dp = [0]*n
dp[1] = a[0]
for i in range(2,n):
    dp[i] = min(dp[i-2] + b[i-2], dp[i-1] + a[i-1])

#逆走してどこの部屋が最適か探す
ans = []
cur = n #現在地
for _ in range(n): #多くともn回までしかさかのぼらない。
    ans.append(cur)
    if cur == 1: #スタートの部屋に到達したらやめる
        break

    #どこからcurに移動するのが最適か求める
    if dp[cur-1] == dp[cur-2] + a[cur-2]:
        cur -= 1
    else:
        cur -= 2    

ans.reverse()
ans_str = [str(i) for i in ans]
print(len(ans_str))
print(" ".join(ans_str))