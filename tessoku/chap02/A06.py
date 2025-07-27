N, Q = map(int, input().split())
A = list(map(int, input().split()))
Questions = [list(map(int, input().split())) for i in range(Q)]

for i in range(1,N):
    A[i] += A[i-1]

for i in range(Q):
    L = Questions[i][0] -1
    R = Questions[i][1] -1
    if L != 0:
        print(A[R] - A[L-1])
    else:
        print(A[R])