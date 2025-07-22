import sys
sys.setrecursionlimit(10*6)
if len(sys.argv) == 2:
    sys.stdin = open(sys.argv[1])
import math
from collections import deque
import bisect

#----------------------------------------#

n = int(input())
cnt = 0
for i in range(1,int(math.log2(n)) + 1):
    n //= 2**i
    cnt += math.isqrt(n)
    cnt -= math.isqrt(n) // 2
    n *= 2**i
print(cnt)

'''
初めに2^aを固定し、とりうるb^2の値の個数をカウント
重複をさけたいのでbが二の倍数の時は数えない
'''
