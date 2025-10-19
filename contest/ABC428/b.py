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
n, k = map(int, input().split())
s = input().strip()
t = []
for i in range(n - k + 1):
    t.append(s[i:i + k])
seqs = dict()
m = 0
for seq in t:
    cnt = 0
    for i in range(n - k + 1):
        if s[i:i + k] == seq:
            cnt += 1
    seqs[seq] = cnt
    m = max(m, cnt)
ans = []
for seq in seqs.keys():
    if seqs[seq] == m:
        ans.append(seq)
ans.sort()
print(m)
print(*ans)