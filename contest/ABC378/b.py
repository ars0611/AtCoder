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
N = int(input())
q = []
r = []
for i in range(N):
    q_i, r_i = map(int,input().split())
    q.append(q_i)
    r.append(r_i)

Q= int(input())
for j in range(Q):
    t_j, d_j = map(int, input().split())
    q_t_j = q[t_j-1]
    r_t_j = r[t_j-1]
    if d_j % q_t_j <= r_t_j:
        print(d_j + r_t_j - d_j % q_t_j)
    else:
        print(d_j + q_t_j - d_j % q_t_j + r_t_j)