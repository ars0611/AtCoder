import sys
sys.setrecursionlimit(10**7)
if len(sys.argv) == 2:
    sys.stdin = open(sys.argv[1])
from collections import Counter
from collections import deque
from collections import defaultdict
import bisect
import math
import itertools
import copy

#----------------------------------------#
n = int(input())

digit = deque()
while n > 0:
    digit.appendleft(n % 10)
    n //= 10

ans = 0
for i in range(len(digit)):

    h = 0
    for j in range(i):
        h = h * 10 + digit[j]

    l = 0
    for j in range(i+1, len(digit)):
        l = l * 10 + digit[j]

    ans += 45 * (10 ** (len(digit) - i - 1)) * h
    ans += (10 ** (len(digit) - i - 1)) * (digit[i] * (digit[i] - 1) // 2)
    ans += digit[i] * (l+1)

print(ans)

#1~9の和の塊で見て、くるくる回すイメージ