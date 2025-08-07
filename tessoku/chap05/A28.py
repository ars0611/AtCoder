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

num = 0
for i in range(n):
    
    t_i, a_i = input().split()
    a_i = int(a_i)
    
    if t_i == "+":
        num += a_i
    
    elif t_i == "-":
        num -= a_i
    
    else:
        num *= a_i
        
    num %= 10000
    print(num)