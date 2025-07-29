import sys
sys.setrecursionlimit(10**7)
if len(sys.argv) == 2:
    sys.stdin = open(sys.argv[1])
import math
from collections import deque
import bisect
from collections import defaultdict
import itertools

#----------------------------------------#
n = int(input())
p = list(map(int, input().split()))
q = list(map(int, input().split()))

dict = {} #key := 人iのゼッケン番号, value := 人iとする。

for i in range(n):
    dict[q[i]] = i+1

s = [None]*n
for i in range(n):
    s[i] = str(q[p[dict[i+1]-1]-1])

print(" ".join(s))