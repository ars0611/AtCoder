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

# フェルマーの小定理を用いて,a / bの剰余を求める。
# modが素数であるときのみ用いれる。合成数ならパスカルの三角形とか使おう。
def Fermat_mod(a, b, mod):
    return ((a % mod) * power(b, mod - 2, mod)) % mod
