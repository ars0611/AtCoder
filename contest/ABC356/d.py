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
#10進数nをb進数変換する関数(2 <= b <= 10)
def base10_to_baseb(n,b):
    res = ""
    while n > 0:
        res = f'{n % b}' + res
        n //= b
    if res == "":
        return "0"
    else:
        return res

n, m = map(int, input().split())
mod = 998244353 
m_base_2 = base10_to_baseb(m, 2)
ans = 0
for i in range(len(m_base_2)):
    if m_base_2[-i-1] == "1":
        ans += (n+1) // 2**(i + 1) * 2**i
        if (n+1) % 2**(i + 1) > 2**i:
            ans += (n+1) % 2**(i + 1) - 2**i
    ans %= mod
print(ans % mod)