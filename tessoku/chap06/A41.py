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
n = int(input())
s = input()

ans = False
for i in range(n-2):
    if s[i] == s[i+1] == s[i+2]:
        ans = True
        break

if ans:
    print("Yes")
else:
    print("No")