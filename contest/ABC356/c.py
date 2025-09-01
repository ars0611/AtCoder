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
# 入力の受け取り非常に大変
n, m, k = map(int, input().split())

c = []
a = []
r = []
for i in range(m):
    test = list(input().split())
    
    ci = int(test[0])
    ai = set(list(map(int, test[1:ci+1])))
    ri = test[-1]
    
    c.append(ci)
    a.append(ai)
    r.append(ri)

# 正解のカギの組み合わせを全列挙
p = []
for i in range(1 << len(list(range(n)))):
    pi = []
    for j in range(len(list(range(n)))):
        if i >> j & 1:
            pi.append(j + 1)
    p.append(pi)

# 組み合わせに対して、テストをすべて通ればokなのでそれを数える
ans = 0
for pp in p:
    comp = False
    for i in range(m):
        cnt = 0
        for ppp in pp:
            if ppp in a[i]:
                cnt += 1
        # テストを通ったら次のテストへ
        if cnt >= k and r[i] == "o" or cnt < k and r[i] == "x":
            continue
        # テストを通らなかったらcompをTrueにする
        comp = True
    # すべて通ってたらcompはFalseのままなのでansを1増やす
    if not comp:
        ans += 1

# 出力
print(ans)

# コードが長くて頭がバグる。落ち着いて処理。