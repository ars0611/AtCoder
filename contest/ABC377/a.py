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
s = input()
if s.count('A') == 1 and s.count('B') == 1 and s.count('C') == 1:
    print('Yes')
else:
    print('No')