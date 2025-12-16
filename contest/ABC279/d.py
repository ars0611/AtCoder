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
a, b = map(int, input().split())
def getTime(k):
    return b * k + a / math.sqrt(k + 1)

l = 0
r = a // b
while r - l > 2:
    m_1 = (2 * l + r) // 3
    m_2 = (l + 2 * r) // 3
    if getTime(m_1) < getTime(m_2):
        r = m_2
    else:
        l = m_1
ans = 10 ** 18
for i in range(l, r + 1):
    ans = min(ans, getTime(i))
print(ans)

# 与式は凸関数
# 凸関数最小値は三分探索典型
# n >= a // bのとき, f(n) = b * nとなり、最小値をとり得ないので、最小値を取るnは a // b >= nとわかる
# そこまで見積もれたら三分探索するだけ
