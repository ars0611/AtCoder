import math

# 素因数分解
def prime_factorization(num):
    res = set()
    root_num = math.isqrt(num)
    k = 1
    while k <= root_num:
        if num % k == 0:
            res.add(k)
            res.add(num // k)
        k += 1
    return res