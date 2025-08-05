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
n = int(input())

#エラトステネスのふるい
l = [True]*(n+1)
l[0] = False
l[1] = False

#生き残りの最小の数を残し、その倍数をFalseにする
for i in range(2,math.isqrt(n)+1):
    
    #生き残ってないので飛ばす
    if not l[i]:
        continue
    
    #固定したiの倍数を消してく
    k = 2*i
    while k <= n:
        l[k] = False
        k += i
    
#Trueが生き残りであり素数であるのでそれを出力
for i in range(n+1):
    if l[i]:
        print(i)