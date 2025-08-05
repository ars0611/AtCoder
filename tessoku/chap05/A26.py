import sys
sys.setrecursionlimit(10**7)
if len(sys.argv) == 2:
    sys.stdin = open(sys.argv[1])
import math
from collections import deque
import bisect
from collections import defaultdict
import itertools
import copy

#----------------------------------------#
q = int(input())

for i in range(q):
    comp = True
    x_i = int(input())
    k = 2
    while k <= math.isqrt(x_i):
        if x_i % k == 0:
            comp = False
            break
        k += 1
    if comp:
        print("Yes")
    else:
        print("No")

#O(q*math.sqrt(x_i)) <= 10**4 * math.sqrt(3 * 10**5)でギリギリセーフ？