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
a,b = map(int, input().split())

#繰り返し二乗法
ans = 1
while b > 0:
    #指数bを二進変換して、ビットが立っている箇所のみ累乗項をかけていくイメージ
    if b % 2 == 1:
        ans = ans * a % (10**9 + 7)
    a = a * a % (10**9 + 7)
    b //= 2

#出力
print(ans)