import sys
sys.setrecursionlimit(10**7)
if len(sys.argv) == 2:
    sys.stdin = open(sys.argv[1])
from collections import Counter, deque, defaultdict
from sortedcontainers import SortedSet, SortedList, SortedDict
import heapq, bisect, math, itertools, copy

#----------------------------------------#
#入力
n = int(input())

p = [] # p[i] := i+1桁の回文数の個数
for i in range(20): #多分40桁の回文数までの個数をnが越えることはない
    p.append(9 * (10**i))
    p.append(9 * (10**i))

#累積和(1-index)
s = [0]
for pi in p:
    s.append(s[-1] + pi)

ans_digit = bisect.bisect_left(s, n) #n番目の回文数が何桁か
k = n - s[ans_digit - 1] - 1 #その桁数の中で求める答えがk番目
half = (ans_digit + 1) // 2 #回文数の左半分の桁数(中央を含む)
base = 10**(half - 1) #左半分の桁数の最小値
left_num = base + (k - 1) #k番目の左半分
left_str = str(left_num)

if ans_digit % 2 == 1:
    # 奇数桁の回文数
    right_str = left_str[-2::-1]
else:
    # 偶数桁の回文数
    right_str = left_str[::-1]

print(left_str + right_str)

# nの制約が大きいことから回文数を列挙していくことが難しいことは容易に気付ける
# そこで、回文数を桁数ごとに何個あるか実験してみると、個数の法則性に気付ける
# 各桁の回文数の数の累積和を取ると、にぶたんで求めたい回文数が何桁かを高速に求められる
#|-ここまでは自明だった

# 回文数問題の典型だが、左半分を決めれば右半分が自動的に決まることを利用する
# 左半分の最少にいくつか足すことで、その桁数の中で何番目かを表現できる
# ただ、桁数の偶奇に注意する必要がある

# palindromicほんま勘弁