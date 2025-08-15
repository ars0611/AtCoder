import sys
sys.setrecursionlimit(10**7)
if len(sys.argv) == 2:
    sys.stdin = open(sys.argv[1])
from collections import Counter
from collections import deque
from collections import defaultdict
from sortedcontainers import SortedSet, SortedList, SortedDict
import heapq
import bisect
import math
import itertools
import copy

#----------------------------------------#
s = input()
dict_ch = {}
for i in range(len(s)):
    dict_ch[s[i]] = i + 1

ans = 0
cur = dict_ch["A"]
for ch in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
    ans += abs(dict_ch[ch] - cur)
    cur = dict_ch[ch]
print(ans)