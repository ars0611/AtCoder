import math

# 素数判定
def is_prime(num):
    root_num = math.isqrt(num)
    k = 2
    while k <= root_num:
        if num % k == 0:
            return False
        k += 1
    return True