n = int(input())
ans = 0
i = 0
while n >  0:
    ans += n % 10 * 2**i
    n //= 10
    i += 1
print(ans)