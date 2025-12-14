# nCrをモジュールなしで求める。

def combination(n, r):
    fac_n = 1
    fac_r = 1
    fac_n_minus_r = 1
    for i in range(n, 0, -1):
        fac_n *= i

        if r >= i:
            fac_r *= i

        if n - r >= i:
            fac_n_minus_r *= i

    return fac_n // (fac_r * fac_n_minus_r)
