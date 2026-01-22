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
s = input().strip()

# nex[i][j] :- 文字iがj文字目以降に出る際の最小のindex
nex = [[-1]*n for _ in range(26)]
for i in range(n - 1, -1, -1):
    if i < n - 1:
        for j in range(26):
            nex[j][i] = nex[j][i + 1]
    idx = ord(s[i]) - ord("a")
    nex[idx][i] = i

cur = -1
ans = []
for i in range(k):
    for j in range(26):
        if n - nex[j][cur + 1] >= k - i and nex[j][cur + 1] > -1:
            ans.append(chr(ord("a") + j))
            cur = nex[j][cur + 1]
            break
print("".join(ans))

# 辞書順最小は前から貪欲！
# 前計算：各文字についてi文字目以降にその文字が出る最小のindex
# 文字列の構成：k文字作るので1文字目から順に文字の辞書順が小さいほうから貪欲に決める
#             ある文字を採用したとき、残り必要な文字数がその後ろにあるなら採用
# ToDo: nexテーブルをライブラリ化
