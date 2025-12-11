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
#----------------------------------------#
s = input().strip()
chSet = [set() for _ in range(len(s))]
brkSiz = 0
for i in range(len(s)):
    if s[i] == "(":
        brkSiz += 1
        chSet[brkSiz] = chSet[brkSiz - 1].copy()
    elif s[i] == ")":
        if brkSiz:
            brkSiz -= 1
    else:
        if s[i] in chSet[brkSiz]:
            print("No")
            break
        chSet[brkSiz].add(s[i])
else:
    print("Yes")

# やはり累積和、累積和がすべてを解決する
# 最も内側のかっこの中身からpopしていくので、何重目のかっこを見ているのか保持しつつ、外側でどの文字を箱に入れたか管理したらいい感じか
