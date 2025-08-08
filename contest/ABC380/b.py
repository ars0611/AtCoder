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
s = input()
a = []

i = 1
cnt = 0
while i < len(s):
    if s[i] == "-":
        cnt += 1
    else:
        a.append(cnt)
        cnt = 0
    i += 1

print(*a)