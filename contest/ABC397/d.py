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
n = int(input())

# x-y := d とすると与式を変形して d**3 <= n <= 10**18 すなわちd <= 10 ** 6 が言える
# これを用いて与式を変形すると 3*d*x**2 - 3*d*x + d**3 - n = 0
# dを全探索し、上式を満たす整数xが存在するなら、(x, x-d)が答え
# xをどう探索するか
# 二分探索で二次方程式に正の整数解あるか見たら間に合うのか
d = 1
for d in range(1, 10**6 + 1):
    if n % d != 0:# d(3*x**2 - 3*d*x + d**2) = n からn / dが整数でないなら意味ない
        continue
    # 二分探索で整数解が存在するか判定
    l = 0
    r =  10**9 + 1
    while r - l > 1:
        m = (l + r) // 2
        if 3 * d * m**2 - 3 * d**2 * m + d**3 >= n:
            r = m
        else:
            l = m
        if 3 * d *  m**2 - 3 * d**2 * m + d**3 - n == 0 and m-d != 0:
            print(m, m-d)
            exit()
print(-1)

# なんやこの数学問題