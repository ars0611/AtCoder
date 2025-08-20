import sys
sys.setrecursionlimit(10**7)
if len(sys.argv) == 2:
    sys.stdin = open(sys.argv[1])
from collections import Counter
from collections import deque
from collections import defaultdict
from sortedcontainers import SortedSet, SortedList, SortedDict
import heapq
import bisect
import math
import itertools
import copy

#----------------------------------------#
#入力
n, m = map(int, input().split())
a = list(map(int, input().split()))

#a_iをmod mに変換
a = [a_i % m for a_i in a]
#累積modを2周分準備
a += a
s = [0]
for a_i in a:
    s.append((s[-1] + a_i) % m)
#累積modの出現回数をカウント
cnt_mod = [0]*m
for i in range(n):
    cnt_mod[s[i]] += 1
#s>tもカウントしたいので,2周目の休憩所1から累積modを見る
#累積modの値が同じ休憩所から,その休憩所まではmの倍数歩で来れる(これは言われてみれば確かに自明)
#見た休憩所と累積modが等しい休憩所の数をカウントしていくが,一周前のところから持ってきて,答えに加算したら休憩所が一つずれるから,見たところの1周前のやつはカウントから除外する
#言語化がむずすぎる。湖の円周を2周分を数直線にして,中点を終点として,長さnで見ていくイメージ
ans = 0
for i in range(n, 2*n):
    cnt_mod[s[i-n]] -= 1
    ans += cnt_mod[s[i]]
    cnt_mod[s[i]] += 1

#出力
print(ans)