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
# 入力
n, k = map(int, input().split())
s = input().strip()

ans = list(s)
for i in range(n):
    # ?がoか.で確定できるなら確定させていく
    if ans[i] != "?" or n == 1:
        continue
    
    # 先頭と末尾は片隣しか見ないので例外処理
    if i == 0 and ans[i + 1] == "o":
        ans[i] = "."
    if i == n - 1 and ans[i - 1] == "o":
        ans[i] = "."

    # 両隣見るとき
    if 0 < i < n - 1:
        if ans[i - 1] == "o" or ans[i + 1] == "o":
            ans[i] = "."

# 尺取りで?のみからなる連続部分列の長さを得る
l = 0
r = 0
cnt = 0
continuous = [] # ?の連続部分列の長さを格納
continuous_start = [] # ?の連続部分列が始まるidxを格納
while r < n:
    if ans[l] != "?":
        cnt = 0
        l += 1
        r = l
        continue
    if ans[l] == ans[r] == "?":
        cnt += 1
        r += 1
    else:
        continuous.append(cnt)
        continuous_start.append(l)
        l = r

if ans[n - 1] == "?":
    continuous.append(cnt)
    continuous_start.append(l)

# 置けるoの個数の最大数
max_o = 0
for i in range(len(continuous)):
    max_o += continuous[i] // 2
    if continuous[i] % 2 == 1:
        max_o += 1

# すでにk個のoを置けている場合
if s.count("o") == k:
    for i in range(n):
        if ans[i] =="?":
            ans[i] ="."

if max_o == k - s.count("o"):
    for i in range(len(continuous)):
        # ?の連続部分列の長さが奇数ならmax_oの実現のためには左詰め
        # 偶数なら右詰めでも変わらない
        if continuous[i] % 2 == 0:
            continue

        # 左詰め
        j = continuous_start[i] 
        cnt = 0
        cmp = True #oを置いて良いか
        while cnt < continuous[i]:
            if cmp:
                ans[j] = "o"
            else:
                ans[j] = "."
            cmp = not cmp
            j += 1
            cnt += 1

# max_o > k ならば最初にやった.だけ確定させるだけでok

# 出力
output = ""
for i in range(n):
    output += ans[i]
print(output)