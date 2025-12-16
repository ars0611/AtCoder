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

k = int(input())
soe = SieveOfEratosthenes(k)
div = soe.getPrimeFactors(k)

ans = 0
for factor, power in div.items():
    cnt = 0
    i = 1
    while cnt < power:
        temp = 0
        num = factor * i
        while num % factor == 0:
            temp += 1
            num //= factor
        i += 1
        cnt += temp
    ans = max(ans, (i - 1) * factor)
print(ans)
