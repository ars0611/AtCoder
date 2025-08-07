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
#入力
n = int(input())

#約数の個数が9個になりうるのは平方数であるため、math.sqrt(n)以下の範囲を探索
limit = math.isqrt(n)

#エラトステネスのふるいで素数列挙
l = [True]*(limit+1)
l[0] = False
l[1] = False

#Trueの最小の数を残し、その倍数をFalseにする
for i in range(2,limit+1):
    
    #Falseは飛ばす
    if not l[i]:
        continue
    #固定したiの倍数をiを除いてFalseにする
    k = 2*i
    while k <= limit:
        l[k] = False
        k += i
    
#Trueは素数であるのでそれをprimeに格納
prime = []
for i in range(limit+1):
    if l[i]:
        prime.append(i)

#math.sqrt(n)以下の数で約数の個数が4つであるものが条件を満たす。
#i.e. math.sqrt(n)以下かつ「二つの素数の積で表せるか素数の4乗で表せる」数が条件を満たす。
ans = 0
for i in range(len(prime)):
    if prime[i] ** 4 <= limit:
        ans += 1
    for j in range(i+1, len(prime)):
        val = prime[i] * prime[j]
        if val <= limit:
            ans += 1
        else:
            break
print(ans)
