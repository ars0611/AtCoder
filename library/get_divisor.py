import math

# 約数の列挙
def get_divisor(num):
    res = set()
    root_num = math.isqrt(num)
    k = 1
    while k <= root_num:
        if num % k == 0:
            res.add(k)
            res.add(num // k)
        k += 1
    return res
