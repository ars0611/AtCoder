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
dict_s = {}
for _ in range(n):
    s_i = input()
    dict_s[len(s_i)] = s_i

sorted_key = sorted(dict_s.keys())

for i in sorted_key:
    print(dict_s[i],end="")
