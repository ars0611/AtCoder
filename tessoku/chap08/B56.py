import sys
sys.setrecursionlimit(10**7)
if len(sys.argv) == 2:
    sys.stdin = open(sys.argv[1])
from collections import Counter
from collections import deque
from collections import defaultdict
import heapq
import bisect
import math
import itertools
import copy
from sortedcontainers import SortedSet, SortedList, SortedDict

#----------------------------------------#
n, q = map(int, input().split())
s = input()

#文字列ハッシュ化
#アルファベットを0-25の整数に変換
t = list(map(lambda c: (ord(c) - ord('a')), s))

#100**nを前計算
mod = 10**9 + 7
power100 = [1] * (n + 1)
for i in range(n):
    power100[i + 1] = power100[i] * 100 % mod

#h_f[i] := 先頭からi文字目までのハッシュ値
#h_b[i] := 末尾からi文字目までのハッシュ値
h_f = [0] * (n + 1)
h_b = [0] * (n + 1)
for i in range(n):
    h_f[i + 1] = (h_f[i] * 100 + t[i]) % mod
    h_b[i + 1] = (h_b[i] * 100 + t[n - 1 - i]) % mod

#ハッシュ値を計算する関数
def get_hash_f(l, r):
    return (h_f[r] - h_f[l - 1] * power100[r - l + 1]) % mod

def get_hash_b(l, r):
    return (h_b[n - l + 1] - h_b[n - r] * power100[r - l + 1]) % mod

for i in range(q):
    l,r = map(int, input().split())
    if get_hash_f(l, r) == get_hash_b(l, r):
        print("Yes")
    else:
        print("No")
