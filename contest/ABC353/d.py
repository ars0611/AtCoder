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
def check_digit(k):
    res = 1
    while k > 0:
        if k // 10 > 0:
            res += 1
        k //= 10
    return res

mod = 998244353
n = int(input())
a = list(map(int, input().split()))
s = [a[0]]
digits = []
for i in range(n):
    digits.append(10 ** check_digit(a[i]))

for i in range(1,n):
    digits[i] += digits[i-1]
    s.append(s[-1] + a[i])

ans = 0
for i in range(n-1):
    ans += ((a[i]*(digits[n-1] - digits[i])) % mod + (s[n-1] - s[i]) % mod) % mod
ans %= mod
print(ans)