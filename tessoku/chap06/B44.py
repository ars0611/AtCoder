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
n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]

#t[i] := 操作後のi+1行目は元のgridのどの行か
t = [i for i in range(n)]
q = int(input())
for _ in range(q):
    
    query = list(map(int, input().split()))
    x = query[1] - 1
    y = query[2] - 1

    #交換処理
    if query[0] == 1:
        w =t[x]
        t[x] = t[y]
        t[y] = w

    #取得処理
    else:
        print(grid[t[x]][y])