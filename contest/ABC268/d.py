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
def insBar(k):

n, m = map(int, input().split())
s = [input().strip() for _ in range(n)]
t = set(input().strip() for _ in range(m))
cnt = 16 - sum(len(s[i]) for i in range(n)) - (n - 1)
for p in itertools.permutations(s):
    sp = list(p)
    print(sp)

# 再帰でアンダースコアを付け加えたいんだけど実装力がないので寝る
