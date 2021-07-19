def f_sum(N):
    return N * (N+1) // 2

def FlyToCentauri(X,Y):
    Fly_Dis = Y - X
    Jump = 0
    history = 0

    while Fly_Dis > 0:

        Jump_dn = f_sum(Jump)

        if Fly_Dis > Jump_dn + Jump:
            Jump += 1
        elif Fly_Dis < Jump_dn:
            Jump -= 1

        Fly_Dis -= Jump
        history += 1

    return history

N = int(input())
for _ in range(N):
    X, Y = map(int,input().split())
    print(FlyToCentauri(X,Y))

