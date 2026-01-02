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
n, k = map(int, input().split())
a = list(map(int, input().split()))
dp = [0]*(n + 1)
for i in range(n + 1):
    for j in range(k):
        if a[j] > i: continue
        dp[i] = max(dp[i], a[j] + i - a[j] - dp[i - a[j]])
print(dp[n])

# 石が残りi個の時に先手が取れる石の数はaj取った後にi - aj個の石を後手が取った残り
# この遷移どうやって思いつけばよかったんだ
# 石の残り数に応じてどの手が最適かが変わることはわかる
# そこから石の数が少ないとこからDPしたくなる
# 先手に注目すると一番とれる選択肢を取りたい
# その後、後手は前計算した最適を取る
# お、じゃあ一番とれる択とって、その個数減らしたときの最適を後手が取って、残りを全部いただこう
# いや、天才にならないと思いつかんて！！！
