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
n = int(input())
a = []
b = []
for i in range(n):
    a_i, b_i = map(int, input().split())
    a.append(a_i)
    b.append(b_i)

#1の時正,0の時負
def check(front, back):
    sum = 0
    for i in range(n):
        
        card_f = a[i]
        card_b = b[i]
        if front == 0:
            card_f = -card_f
        if back == 0:
            card_b = -card_b
        if card_f + card_b >= 0:
            sum += card_f + card_b
    return sum

ans = 0
for i in range(2):
    for j in range(2):
        ans = max(ans, check(i, j))
print(ans)

#各面について,和の絶対値を最大化したいので,和を最大にする場合,最小にする場合それぞれについて全探索
#この解法どうも非自明に感じてしまう
