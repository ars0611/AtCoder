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
n,q = map(int, input().split())

#nest[i] := 巣i+1にいる鳩の数
nest = [1]*n

#key := 鳩i, value := 鳩iがいるnestの要素番号
dict ={i+1:i for i in range(n)}

#鳩が複数いる箱を数える
ans = 0
#query処理
for _ in range(q):
    #query受け取り
    num, *move = map(int,input().split())
    
    #query_1の処理
    if num == 1:
       
        #移動予定の鳩がいる巣に２匹しかいないとき、移動後は１匹なのでansを減らす
        if nest[dict[move[0]]] == 2:
            ans -= 1
        nest[dict[move[0]]] -= 1
        
        #鳩が向かう巣が１匹しかいないとき、移動後は2匹なのでansを増やす
        if nest[move[1]-1] == 1:
            ans += 1
        nest[move[1]-1] += 1
        
        #鳩を移動させる
        dict[move[0]] = move[1]-1

    #query_2の処理        
    else:
        print(ans)