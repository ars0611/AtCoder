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
#入力
n, k = map(int, input().split())
s = list(input())

#start[i] := i+1番目の1の塊の始点, end[i] := i+1番目の1の塊の終点
start = []
end = []
#尺取りで1の塊を得る
l = 0
r = 0
while l < n:
    
    #始点を探す
    if s[l] != "1":
        l += 1
        r = l
    
    #終点をずらす
    elif r < n-1 and s[r] == "1"  or r == n-1 and s[r] == "1":
        r += 1

    #塊が終了したので始点をずらす
    else:
        start.append(l)
        end.append(r-1)
        l = r

#1の塊移動
for i in range(end[k-1] - start[k-1] + 1):
    s[end[k-2] + i+1] = "1"
    s[start[k-1] + i] = "0"

#出力
print("".join(s))