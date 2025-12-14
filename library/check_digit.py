# 整数nの桁数を求める関数
def check_digit(n):
    res = 1
    while n > 0:
        if n // 10 > 0:
            res += 1
        n //= 10
    return res
