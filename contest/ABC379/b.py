import sys
sys.setrecursionlimit(10**7)
if len(sys.argv) == 2:
    sys.stdin = open(sys.argv[1])
from collections import Counter
from collections import deque
from collections import defaultdict
import bisect
import math
import itertools
import copy

#----------------------------------------#
n, k = map(int, input().split())
s = input()

i = 0
cnt = 0
while i <= (n-k):
    if s[i:i+k] == "O" * k:
        cnt += 1
        i += k
    else:
        i += 1

print(cnt)