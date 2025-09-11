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
# スライドmax
def slide_max(list, k):
    window = deque()
    max_num_in_window = []
    for i in range(len(list)):
        if window and window[0] < i - k + 1:
            window.popleft()
        while window and list[window[-1]] < list[i]:
            window.pop()
        window.append(i)
        if i >= k - 1:
            max_num_in_window.append(list[window[0]])
    return max_num_in_window

# スライドmin
def slide_min(list, k):
    window = deque()
    min_num_in_window = []
    for i in range(len(list)):
        if window and window[0] < i - k + 1:
            window.popleft()
        while window and list[window[-1]] > list[i]:
            window.pop()
        window.append(i)
        if i >= k - 1:
            min_num_in_window.append(list[window[0]])
    return min_num_in_window

# 入力
n, k = map(int, input().split())
p = list(map(int, input().split()))

d = [0] * n #idx := pi, value := i
for i, pi in enumerate(p):
    d[pi-1] = i

max_num_in_window = slide_max(d,k)
min_num_in_window = slide_min(d,k)

ans = n
for i in range(n - k + 1):
    ans = min(ans, max_num_in_window[i] - min_num_in_window[i])
print(ans)

# 尺取りらしく累積max,minをとってる感覚か