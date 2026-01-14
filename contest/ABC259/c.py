import sys
if len(sys.argv) == 2:
    sys.stdin = open(sys.argv[1])
sys.setrecursionlimit(10**7)
input = sys.stdin.readline
#----------------------------------------#
import math
import bisect
import itertools
import heapq
from collections import deque
from collections import Counter
from collections import defaultdict
from sortedcontainers import SortedList
from sortedcontainers import SortedSet
from sortedcontainers import SortedDict
from more_itertools import distinct_permutations
from functools import lru_cache
#----------------------------------------#
s = input().strip()
t = input().strip()
if len(s) > len(t):
    print("No")
else:
    zippedS = []
    cnt = 1
    cur = s[0]
    for i in range(1, len(s)):
        if cur == s[i]:
            cnt += 1
        else:
            zippedS.append((ord(cur), cnt))
            cur = s[i]
            cnt = 1
    zippedS.append((ord(cur), cnt))
    zippedT = []
    cnt = 1
    cur = t[0]
    for i in range(1, len(t)):
        if cur == t[i]:
            cnt += 1
        else:
            zippedT.append((ord(cur), cnt))
            cur = t[i]
            cnt = 1
    zippedT.append((ord(cur), cnt))
    if len(zippedS) != len(zippedT):
        print("No")
    else:
        flg = True
        for seg in range(len(zippedS)):
            if (2 <= zippedS[seg][1] <= zippedT[seg][1] or zippedS[seg][1] == zippedT[seg][1]) and zippedS[seg][0] == zippedT[seg][0]: continue
            flg = False
        print("Yes" if flg else "No")

# ToDo: ランレングス圧縮ライブラリ化
