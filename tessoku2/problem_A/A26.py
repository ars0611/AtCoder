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
def is_prime(num):
    root_num = math.isqrt(num)
    k = 2
    while k <= root_num:
        if num % k == 0:
            return False
        k += 1
    return True

q = int(input())
for _ in range(q):
    x = int(input())
    print("Yes" if is_prime(x) else "No")