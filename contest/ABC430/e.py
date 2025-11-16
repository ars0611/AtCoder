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
# sh = StringHash(s)
class StringHash:
    def __init__(self, s, base = 100, mod = 2147483647):
        self.n = len(s)
        self.mod = mod
        self.base = base

        # アルファベットを 0〜25 に変換
        t = [ord(ch) - ord('a') for ch in s]

        # base**i を前計算
        self.power = [1] * (self.n + 1)
        for i in range(self.n):
            self.power[i + 1] = self.power[i] * self.base % self.mod

        # h[i] := 先頭から i 文字目までのハッシュ値
        self.h = [0] * (self.n + 1)
        for i in range(self.n):
            self.h[i + 1] = (self.h[i] * self.base + t[i]) % self.mod

    # s[l:r](0-index)のハッシュ値
    def get_hash(self, l, r):
        return (self.h[r] - self.h[l] * self.power[r - l]) % self.mod

t = int(input())
for _ in range(t):
    a = input().strip()
    b = input().strip()
    n = len(a)
    sh_a = StringHash(a + a)
    sh_b = StringHash(b)
    hash_b = sh_b.get_hash(0, n)
    for i in range(n):
        hash_a = sh_a.get_hash(i, n + i)
        if hash_a == hash_b:
            print(i)
            break
    else:
        print(-1)