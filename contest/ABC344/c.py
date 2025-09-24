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
a = list(map(int, input().split()))
m = int(input())
b = list(map(int,input().split()))
l = int(input())
c = list(map(int, input().split()))
q = int(input())
x = list(map(int, input().split()))

sum_set = set()
for i in range(n):
    for j in range(m):
        for k in range(l):
            sum_set.add(a[i]+b[j]+c[k])

for i in range(q):
    print("Yes" if x[i] in sum_set else "No")