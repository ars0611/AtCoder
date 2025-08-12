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
#入力
n, d = map(int, input().split())

#job[i] := i+1日目に可能になる仕事の金額リスト
job = [[] for _ in range(d)]
for i in range(n):
    x, y = map(int, input().split())
    job[x-1].append(y)

#job_d[i] := i+1日目時点でできる仕事の金額リスト
job_d = []
ans = 0
for i in range(d):
    
    #i+1日目から可能になる仕事があるなら,job_dに格納
    if job[i] != []:
        for j in range(len(job[i])):
            job_d.append(job[i][j])
    
    #金額について高いほうから貪欲に選びたいのでsort
    job_d.sort()

    #可能な仕事があるなら金額が高いものを選ぶ
    if job_d != []:
        ans += job_d.pop()

print(ans)

#テストケースが弱かったために通ってしまった感