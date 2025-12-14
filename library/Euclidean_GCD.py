# ユークリッドの互除法による最大公約数の求値
def Euclidean_GCD(a, b):
    x = max(a, b)
    y = min(a, b)
    while y > 0:
        tmp = x % y
        x = y
        y = tmp
    return x
