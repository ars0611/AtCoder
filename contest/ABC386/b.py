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
s =input()
ans = 0
i = 0
while i <= len(s)-1:
    if i+1 <= len(s) - 1 and s[i] == s[i+1] == "0":
        i += 2
    else:
        i += 1
    ans += 1
print(ans)