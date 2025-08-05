import sys
sys.setrecursionlimit(10**7)
if len(sys.argv) == 2:
    sys.stdin = open(sys.argv[1])
import math
from collections import deque
import bisect
from collections import defaultdict
import itertools
import copy

#----------------------------------------#
#入力
a, b = map(int, input().split())

#ユークリッドの互除法
l = max(a,b) #割られる数
r = min(a,b) #割る数
w = 0 #保存用
while l % r != 0:
    w = r
    r = l % r
    l = w

#出力
print(r)