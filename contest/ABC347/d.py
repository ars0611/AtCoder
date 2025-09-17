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
    
#b進数nを10進数変換する関数(2 <= b <= 9)
def baseb_to_base10(n, b):
    n = str(n)
    d = len(n)
    res = 0
    for i in range(d):
        res += int(n[i]) * b **(d - 1 - i)
    return res

a, b, c = map(int, input().split())
c_base2 = base10_to_baseb(c, 2)
if a + b < c_base2.count("1") or (a + b - c_base2.count("1")) % 2 != 0:
    print(-1)
    exit()

x = ""
y = ""
for i in range(len(c_base2)):
    if c_base2[i] == "1":
        if a >= b:
            x += "1"
            y += "0"
            a -= 1
        else:
            x += "0"
            y += "1"
            b -= 1
    else:
        x += "0"
        y += "0"

if a == b:
    i = 0
    l = len(x)
    while a > 0:
        if i < l:
            if x[i] == y[i] == "0":
                x = x[:i] + "1" + x[i+1:]
                y = y[:i] + "1" + y[i+1:]
                a -= 1
            i += 1
        else:
            x = "1" + x
            y = "1" + y
            a -= 1
    if len(x) <= 60:
        ans = [baseb_to_base10(int(x),2), baseb_to_base10(int(y), 2)]
    else:
        ans = [-1]
else:
    ans = [-1]
print(*ans)