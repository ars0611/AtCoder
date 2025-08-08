import sys
sys.setrecursionlimit(10**7)
if len(sys.argv) == 2:
    sys.stdin = open(sys.argv[1])
from collections import Counter
from collections import deque
from collections import defaultdict
import bisect
import math
import itertools
import copy

#----------------------------------------#
n, a, b = map(int,input().split())

#dp[i] := 石がi個残っていて、Trueなら勝ち,Falseなら負けが確定する
dp = [False]*(n+1)

#石がi個残っているとき、そこからaかb個取ってFalseにできるなら、相手が負け確定になるのでdp[i]をTrueにする
for i in range(min(a,b), n+1):
        if 0 <= i-1 and dp[i-a] == False or 0 <= i-b and dp[i-b] == False:
            dp[i] = True
        else:
            dp[i] = False

if dp[n]:
    print("First")
else:
    print("Second")