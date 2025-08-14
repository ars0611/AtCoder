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
n, s, t = map(int, input().split())
g = [list(map(int, input().split())) for _ in range(n)]


ans = []
#順列全探索
l = list(itertools.permutations(range(n)))
for p in l:

    #照射方向についてビット全探索
    for i in range(1 << len(p)):
        
        #各照射順について,所要時間を計算
        #現座地の座標をcur_x,yで管理
        cur_x = 0
        cur_y = 0
        time = 0
        
        #ビットが1であれば順方向に,0であれば逆方向に照射
        for j in range(len(p)):
            a = g[p[j]][0]
            b = g[p[j]][1]
            c = g[p[j]][2]
            d = g[p[j]][3]
            
            if i >> j & 1:
                time += math.sqrt((cur_x - a)**2 + (cur_y - b)**2) / s
                time += math.sqrt((a - c)**2 + (b - d)**2) / t
                cur_x = c
                cur_y = d
            
            else:
                time += math.sqrt((cur_x - c)**2 + (cur_y - d)**2) / s
                time += math.sqrt((a - c)**2 + (b - d)**2) / t
                cur_x = a
                cur_y = b
        
        ans.append(time)

print(min(ans))