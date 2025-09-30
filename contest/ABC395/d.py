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
n, q = map(int, input().split())
pigeons = [i for i in range(n)] #鳩iのセットの旗
box = [i for i in range(n)] # 巣iにいる旗
swap = [i for i in range(n)] # 旗iのいる巣
for _ in range(q):
    op = list(map(int, input().split()))
    
    if op[0] == 1:
        a, b = op[1] - 1, op[2] - 1
        pigeons[a] = box[b]
    
    # 交換処理がミソすぎる
    elif op[0] == 2:
        a, b = op[1] - 1, op[2] - 1
        box[a], box[b] = box[b], box[a]
        swap[box[a]], swap[box[b]] = swap[box[b]], swap[box[a]] 

    else:
        a = op[1] - 1
        print(swap[pigeons[a]] + 1)

# 鳩iとセットで移動する旗的なのを管理する