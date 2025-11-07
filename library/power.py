# return a ** b % mod
# 繰り返し二乗法による累乗の剰余計算 <- しょーみpow(a, b, mod)で良い
def power(a, b, mod):
    # 指数を2進変換した際のビット数を求める。
    k = 0
    while 1 << k <= b:
        k += 1

    # 繰り返し二乗法
    res = 1
    p = a
    for i in range(k):
        if (1 << i) & b:
            res = (res * p) % mod
        p = (p * p) % mod
    
    return res
