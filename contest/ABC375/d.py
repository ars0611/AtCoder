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

#sに含まれる各文字について,その文字をkeyとして,その文字が存在するindexをvalueにlistとして格納
dict_s = defaultdict(list)
for i in range(len(s)):
    dict_s[s[i]].append(i)

#空でないvalueのkeyをリスト化
dict_key_list = list(set(s))

ans = 0
#list化したkeyを順に参照
for key in dict_key_list:
    
    #keyが存在するindexのリストを取得
    ch_index_list = dict_s[key]
    
    #indexについて累積和を取る
    total = [0]*(len(ch_index_list) + 1)
    for i in range(len(ch_index_list)):
        total[i+1] = total[i] + ch_index_list[i]

    #ch_index_list[k]を固定して,固定したそれ以下のindexをiとし,jが何通りあるかをansに加算する
    for k in range(1,len(ch_index_list)):
        ans += k * ch_index_list[k] - total[k] - k
print(ans)

#累積和つかうと楽になりそうなことまでは気づけたけど,line37,38の足し引きで詰まってしまって頭わり～！！！