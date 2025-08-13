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

if n < 3:
    print(0)
    exit()

else:
    ans = 0
    for i in range(1,n-1):
        if s[i-1] == s[i+1] == "#" and s[i] == ".":
            ans += 1

    print(ans)