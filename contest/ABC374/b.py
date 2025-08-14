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
t = input()

for i in range(min(len(s), len(t))):
    if s[i] != t[i]:
        print(i + 1)
        exit()

if len(s) != len(t):
    print(min(len(s), len(t)) + 1)
    exit()

print(0)