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
#----------------------------------------#
n, x, y = map(int, input().split())
a = list(map(int, input().split()))
pos = [(0, 0), (a[0], 0)]

# graph張っていけそうな感じするけどどうなん
# graph張ると頂点数が2**nで爆発するか。じゃあDP？
# 縦横にaiの距離で移動できるわけで添え字の偶奇で縦か横かは決まってる
# 縦横それぞれ正負どっちにいくか決めてその和がx,yにいけるかどうかで判定できそう
# bit全探索では2**nでやばいか
