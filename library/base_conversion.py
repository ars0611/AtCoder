#10進数nをb進数変換する関数(2 <= b <= 10)
def base10_to_baseb(n,b):
    res = ""
    while n > 0:
        res = f'{n % b}' + res
        n //= b
    if res == "":
        return "0"
    else:
        return res

#b進数nを10進数変換する関数(2 <= b <= 9)
def baseb_to_base10(n, b):
    n = str(n)
    d = len(n)
    res = 0
    for i in range(d):
        res += int(n[i]) * b **(d - 1 - i)
    return res