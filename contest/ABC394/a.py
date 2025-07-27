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
s = input()
ans= []
for i in s:
    if i == "2":
        ans.append(i)
print("".join(ans))