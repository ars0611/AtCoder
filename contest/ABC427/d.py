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
    n, m, k = map(int ,input().split())
    s = input().strip()
    
    graph = [[] for __ in range(n)]
    for i in range(m):
        u, v = map(int, input().split())
        u -= 1
        v -= 1
        graph[u].append(v)
    
    dp = [[False] * n  for _ in range(2 * k + 1)]
    dp[0] = [(c == "A") for c in s]
    for i in range(1, 2 * k + 1):
        if i % 2 == 0:
            for cur in range(n):
                win = False
                for nxt in graph[cur]:
                    if dp[i - 1][nxt]:
                        win = True
                dp[i][cur] = win
        else:
            for cur in range(n):
                win = True
                for nxt in graph[cur]:
                    if not dp[i - 1][nxt]:
                        win = False
                dp[i][cur] = win
    print("Alice" if dp[2*k][0] else "Bob")