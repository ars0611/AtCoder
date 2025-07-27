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
s = list(input())

#末尾から参照していく
for i in range(1,len(s)+1):
    if -i-1 >= -len(s) and s[-i-1] =="W" and s[-i] == "A":
        s[-i-1] = "A"
        s[-i] = "C"
print("".join(s))