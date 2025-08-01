import sys
sys.setrecursionlimit(10**7)
if len(sys.argv) == 2:
    sys.stdin = open(sys.argv[1])
import math
from collections import deque
import bisect
from collections import defaultdict
import itertools

#----------------------------------------#
q = int(input())

snakes_length_sum = [0]
snakes_dequeue_sum = 0
dequeue_cnt = 0 
for _ in range(q):
    query = list(map(int, input().split()))
    
    if query[0] == 1:
        snakes_length_sum.append(snakes_length_sum[-1] + query[1])
    
    elif query[0] == 2:
        snakes_dequeue_sum = snakes_length_sum[dequeue_cnt+1]
        dequeue_cnt += 1
    else:
        print(snakes_length_sum[query[1]-1 + dequeue_cnt] - snakes_dequeue_sum)

#読みにく