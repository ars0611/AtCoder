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



# 素因数分解による解法
'''
def prime_factorization(num):
    res = set()
    root_num = math.isqrt(num)
    k = 1
    while k <= root_num:
        if num % k == 0:
            res.add(k)
            res.add(num // k)
        k += 1
    return res

a, b = map(int, input().split())
div_a = prime_factorization(a)
div_b = prime_factorization(b)
div_a = sorted(list(div_a), reverse=True)

for num in div_a:
    if num in div_b:
        print(num)
        break
'''
