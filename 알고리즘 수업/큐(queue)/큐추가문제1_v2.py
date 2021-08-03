N = int(input())

set = 2

while True:
    if N <= 2 :
        print(N)
        break

    set = set * 2

    if set >= N:
        print((N - (set // 2))*2)
        break
    