import sys
sys.setrecursionlimit(10**7)
if len(sys.argv) == 2:
    sys.stdin = open(sys.argv[1])
import math
from collections import deque
import bisect
from collections import defaultdict

#----------------------------------------#
n = int(input())
a = list(map(int, input().split()))

#aの要素がすべて異なる
if len(a) == len(set(a)):
    print(-1)
    exit()

#aの全要素についてそれが現れる要素番号を辞書型に保存
dict_a = defaultdict(int)
for i,v in enumerate(a) :
    if dict_a[v] == 0:
        dict_a[v] = [i]
    else:
        dict_a[v].append(i)

#複数回現れるAiについて、Aiが現れる1回目と２回目の要素番号の距離が最も短いものが答え
ans = n
for value in dict_a.values():
    if len(value) >= 2:
        value.sort()
        ans = min(ans,value[1] - value[0] + 1)

print(ans)