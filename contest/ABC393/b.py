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
s= input()
cnt= 0
for i in range(len(s)):
    for j in range(i, len(s)):
        for k in range(j,len(s)):
            if s[i] == "A" and s[j] == "B" and s[k] == "C" and j-i == k-j:
                cnt += 1
print(cnt)