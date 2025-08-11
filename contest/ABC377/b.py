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
grid = []
for i in range(8):
    s_i = list(input())
    grid.append(s_i)

safe_rows = 0
safe_cols = 0
for i in range(8):
    
    #駒を取られない行を数える
    if grid[i].count(".") == 8:
        safe_rows += 1

    #i列目に固定して駒を取られない列を数える
    for j in range(8):
        if grid[j][i] == "#":
            break
        if j == 7:
            safe_cols += 1

#駒を取られないマスの数を出力
print(safe_rows * safe_cols)