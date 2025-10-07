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
#10進数nをb進数変換する関数(2 <= b <= 10)
def base10_to_baseb(n,b):
    res = ""
    while n > 0:
        res = f'{n % b}' + res
        n //= b
    if res == "":
        return "0"
    else:
        return res
    
n = int(input())
cnt = 0
num = 0
while cnt < n:
    num_base4 = base10_to_baseb(num, 4)
    i = 0
    ans = 0
    s = 0
    while i < len(num_base4):
        s += int(num_base4[i])
        i += 1
    if s == 3:
        cnt += 1
    num += 1

j = 0
ans = 0
while j < len(num_base4):
    ans += int(num_base4[j]) * int("1"*(len(num_base4) - j))
    j += 1
print(ans)

# n小さくてありがとう。絶対非想定解。実行時間1718ms <- これはなに