import sys
if len(sys.argv) == 2:
    sys.stdin = open(sys.argv[1])
sys.setrecursionlimit(10**7)
input = sys.stdin.readline
#----------------------------------------#
import math
import bisect
import itertools
import heapq
from collections import deque
from collections import Counter
from collections import defaultdict
from sortedcontainers import SortedList
from sortedcontainers import SortedSet
from sortedcontainers import SortedDict
from more_itertools import distinct_permutations
#----------------------------------------#
n = int(input())
a = list(map(int, input().split()))

g = 0
for ai in a:
    g = math.gcd(g, ai)
ans = 0
for ai in a:
    ai //= g
    while ai % 2 == 0 or ai % 3 == 0:
        if ai % 2 == 0:
            ans += 1
            ai //= 2
        if ai % 3 == 0:
            ans += 1
            ai //= 3
    if ai != 1:
        ans = -1
        break
print(ans)

# a = [8, 9]みたいなケースは不可と考えてしまっていたせいで、解けなかった
# ai = 2**pi * 3**qi * ri
# ri != rjなるi != jがあるなら答えは-1
# ないならmin(p), min(q)を目指して、ans += pi - min(p) + qi - min(q)
# gcd用いれば、指数のかぶってる部分やriを消せる
# できるだけ2, 3で割って、徐々に全てを大きくする方針を取るともっと自然
