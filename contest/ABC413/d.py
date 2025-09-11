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
t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    
    pos = 0 # 正の項の数
    for i in range(n):
        if a[i] > 0:
            pos += 1
    neg = n - pos # 負の項の数
    
    # aiの符号と絶対値で持ち直す
    abs_a = []
    for i in range(n):
        if a[i] > 0:
            op = 0
        else:
            op = 1
        abs_a.append((abs(a[i]), op))
    abs_a.sort()

    ans = True
    # 絶対値が等比か
    for i in range(2,n):
        if abs_a[1][0] * abs_a[i-1][0] == abs_a[i][0] * abs_a[0][0]:
            continue
        ans = False
    
    # 符号が混在してるとき隣り合った数の符号が同じとき、満たさない
    for i in range(1, n):
        if (pos != n and neg != n) and abs_a[i][1] == abs_a[i-1][1]:
            ans = False
    
    # 数列の絶対値がすべて等しい場合のみ符号数の判定をする
    if len(list(set([abs(a[i]) for i in range(n)]))) == 1:
        # a内の項に正負が混在しているなら、符号数が二分割されていれば等比数列にできる
        if pos == n or neg == n or abs(pos - neg) <= 1:
            ans = True

    if ans:
        print("Yes")
    else:
        print("No")

# 絶対値がすべて等しい数列を考慮出来ていなかった。問題のテストケースが弱いのは意図されているから自分で落ちてるケースを考えよう。ＧＰＴでデバッグする怠惰しぐさは成長しない。