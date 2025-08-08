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
s = input()
q = int(input())
k = list(map(int, input().split()))

#10進数valueをbase進数変換
def base10int(value,base):
    A = []
    while value > 0:
        A.append(str(value % base))
        value //= base
    return  str(''.join(A[::-1]))

#k_iが何個目の操作に含まれるか
c = []
for k_i in k:
    c.append((k_i-1) // len(s))

for i,c_i in enumerate(c):
    if base10int(c_i,2).count("1") % 2 == 1:
        print(s[(k[i]-1) % len(s)].swapcase(), end = " ")
    else:
        print(s[(k[i]-1) % len(s)], end = " ")

'''
実験
aB aBAb aBAbAbaB aBAbAbaBAbaBaBAb
00 0011 00111100 0011110011000011
'''