import sys
sys.setrecursionlimit(10**7)
if len(sys.argv) == 2:
    sys.stdin = open(sys.argv[1])
input = sys.stdin.readline
from collections import Counter, deque, defaultdict
from sortedcontainers import SortedSet, SortedList, SortedDict
from more_itertools import distinct_permutations
import heapq, bisect, math, itertools

#----------------------------------------#
# 入力
n = int(input())
s = input()

# Aの出現したidxを記録
a = []
for i, si in enumerate(s):
    if si == "A":
        a.append(i)

# 目標の文字列t1,t2とidx比較して移動距離の和を取る
t1 = [2 * i for i in range(len(a))] # ABAB...のAのidx
t2 = [2 * i + 1 for i in range(len(a))] # BABA...のAのidx
ans1 = 0
ans2 = 0
for i in range(len(a)):
    ans1 += abs(a[i] - t1[i])
    ans2 += abs(a[i] - t2[i])

# 最小の移動距離を出力
print(min(ans1, ans2))

# これ嘘解法だと思ったんだが,なぜ通るのか証明してくれないか？