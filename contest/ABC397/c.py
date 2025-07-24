import sys
sys.setrecursionlimit(10*6)
if len(sys.argv) == 2:
    sys.stdin = open(sys.argv[1])
import math
from collections import deque
from collections import defaultdict
import bisect

#----------------------------------------#
n = int(input())
a = list(map(int, input().split()))
ans = 0

left = set()
right = defaultdict(int)
for i in a:
    right[i] += 1
for i in range(n):
    w = a[i]
    left.add(w)
    right[w] -= 1
    if right[w] == 0:
        del right[w]
    ans = max(ans,len(left) + len(right))

print(ans)

'''
初めに
set1 = set(a[:i])
set2 = set(a[i:])
をfor文でまわしてO(N**2)でTLEしてしまってた。
毎回取得するのを辞めたらよい
dequeも試したが、要素数を調べる際毎回setに変換するはめになってTLE。
dictつかってひとつずつ動かせばO(1)?
'''