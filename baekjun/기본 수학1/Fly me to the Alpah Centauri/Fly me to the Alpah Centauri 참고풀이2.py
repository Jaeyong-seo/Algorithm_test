N = int(input())
for _ in range(N):
    X, Y = map(int,input().split())
    print(int(((Y - X)*4-3)**.5))

    