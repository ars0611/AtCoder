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
from functools import lru_cache
from functools import cmp_to_key
#----------------------------------------#
n, x = map(int, input().split())
s = input().strip()
b = list(format(x, 'b'))
for ch in s:
    if ch == 'U':
        b.pop()
    elif ch == 'L':
        b.append('0')
    else:
        b.append('1')
print(int(''.join(b), 2))

# 確かにビットシフト使えば解けるわ。2倍、1/2倍、2倍+1の計算とかでてきたらこれ思い浮かぶようにしたい
