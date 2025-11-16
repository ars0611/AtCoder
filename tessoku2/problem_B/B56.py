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
#----------------------------------------#
# sh = StringHash(s)
class StringHash:
    def __init__(self, s, base = 100, mod = 2147483647):
        self.n = len(s)
        self.mod = mod
        self.base = base

        # アルファベットを 0〜25 に変換
        t = [ord(ch) - ord('a') for ch in s]
        # tの逆順も変換
        reversed_t = [ord(s[- i - 1]) - ord('a') for i in range(n)]
        
        # base**i を前計算
        self.power = [1] * (self.n + 1)
        for i in range(self.n):
            self.power[i + 1] = self.power[i] * self.base % self.mod

        # h[i] := 先頭から i 文字目までのハッシュ値
        self.h = [0] * (self.n + 1)
        for i in range(self.n):
            self.h[i + 1] = (self.h[i] * self.base + t[i]) % self.mod
        # tの逆順
        self.reversed_h = [0] * (self.n + 1)
        for i in range(self.n):
            self.reversed_h[i + 1] = (self.reversed_h[i] * self.base + reversed_t[i]) % self.mod

    # s[l:r](0-index)のハッシュ値
    def get_hash(self, l, r):
        return (self.h[r] - self.h[l] * self.power[r - l]) % self.mod
    # reversedのs[l:r]のハッシュ値
    def get_reversed_hash(self, l, r):
        return (self.reversed_h[r] - self.reversed_h[l] * self.power[r - l]) % self.mod

n, q = map(int, input().split())
s = input().strip()
sh = StringHash(s)
for _ in range(q):
    l, r = map(int, input().split())
    print("Yes" if sh.get_hash(l - 1, r) == sh.get_reversed_hash(n - r, n - l + 1) else "No")