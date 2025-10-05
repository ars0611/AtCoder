import sys
sys.setrecursionlimit(10**7)
if len(sys.argv) == 2:
    sys.stdin = open(sys.argv[1])
input = sys.stdin.readline
from collections import Counter, deque, defaultdict
from sortedcontainers import SortedSet, SortedList, SortedDict
from more_itertools import distinct_permutations
import heapq, bisect, math, itertools

#----------------------------------------#
t = int(input())
for _ in range(t):
    n = int(input())
    s = input().strip()
    l = 0
    r = 0
    c0 = 0
    c1 = 0
    # 最長の11..1と00..0の部分列を求めてる
    while r < n:
        if s[l] == s[r]:
            r += 1
        else:
            if s[r] == "0":
                c1 = max(r - l, c1)
            else:
                c0 = max(r - l, c0)
            l = r
    if s[r-1] == s[l] == "0":
        c0 = max(r - l, c0)
    elif s[r - 1] == s[l] == "1":
        c1 = max(r - l, c1)
    
    # 最長の部分列はノータッチで、それ以外00..0や11..1にするためにマジで操作
    # 状況に応じて操作回数が１か２は自明
    # これでいけるか
    m0 = s.count("0")
    m1 = s.count("1")
    ans = min(m1 + (m0 - c0)*2 , m0 + (m1 - c1)*2)
    print(ans)