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
from functools import cmp_to_key
#----------------------------------------#
class SieveOfEratosthenes:
    # 初期化
    def __init__(self, n):
        if n < 2: raise ValueError("nは2以上にしてください")
        if n > 10**12: raise ValueError("nは10**12以下にしてください")
        self.n = n
        self.rootN = math.isqrt(n)
        self.dp = [True] * (self.rootN - 1)
        self.setTable()
    
    # 2 <= k <= sqrt(n)について素数かどうかboolでもつ。O(sqrt(n) * loglog(sqrt(n)))
    # dp[i - 2] := 整数iについての情報
    # primeNums := sqrt(n)以下の素数の集合
    def setTable(self):
        self.primeNumsArr = list()
        for i in range(self.rootN - 1):
            if not self.dp[i]: continue
            self.primeNumsArr.append(i + 2)
            num = (i + 2) ** 2
            while num <= self.rootN:
                self.dp[num - 2] = False
                num += i + 2
        return

    # 2 <= k <= sqrt(n)が素数かどうかboolで返す。O(1)
    # sart(n) < k <= nが素数かどうかboolで返す。O(sqrt(k))
    # テーブル外のkは常にfalse
    def isPrime(self, k):
        if k < 2:
            return False
        elif k <= self.rootN:
            return self.dp[k - 2]
        elif k <= self.n:
            rootK = math.isqrt(k)
            for d in self.primeNumsArr:
                if d > rootK: break
                if k % d == 0 :
                    return False
            return True
        else:
            return False

    # 2 <= k <= nを素因数分解し、dictで返す。O(math.sqrt(n) * log(n))
    # テーブル外のkは常に空のdictを返す
    def getPrimeFactors(self, k):
        res = dict()
        if k > self.n or k < 2:
            return res
        rootK = math.isqrt(k)
        for d in self.primeNumsArr:
            if d > rootK: break
            if k % d != 0: continue
            cnt = 0
            while k % d == 0:
                cnt += 1
                k //= d
            res[d] = cnt
            rootK = math.isqrt(k)
            if k == 1:
                break
        if k != 1:
            res[k] = 1
        return res
SoE = SieveOfEratosthenes(10 ** 7)
mod = 998244353
t = int(input())
for _  in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    factors = [dict() for _ in range(n)]
    top1 = defaultdict(int)
    top2 = defaultdict(int)
    for i in range(n):
        factors[i] = SoE.getPrimeFactors(a[i])
        for k, v in factors[i].items():
            if top1[k] <= v:
                top2[k] = top1[k]
                top1[k] = v
            elif top2[k] <= v:
                top2[k] = v
    m = 1
    for k, v in top1.items():
        m *= pow(k, v, mod)
        m %= mod
    l = [0]*n
    for i in range(n):
        res = m
        for k, v in factors[i].items():
            if top1[k] == v:
                res *= pow(pow(k, top1[k] - top2[k], mod), mod - 2, mod)
        l[i] = res % mod
    print(*l)

# 各要素素因数分解
# 全体のgcdを取っておいて、各iの指数を取り除く感覚でやる
# 各素因数の数のtop2つを管理しておけば高速に更新できそう
# 常々modを取る際にネックになるのが除算で取り除く部分だが、逆元の定義を考えると取り除きたい部分の逆元をかけることでできる
