def f_sum(N):#---------------비용 함수
    return N * (N+1) // 2

def FlyToCentauri(X,Y):
    Fly_Dis = Y - X#--------남은거리
    Jump = 0#---------------이동거리
    history = 0#------------이동횟수

    while Fly_Dis > 0:
        Jump_dn = f_sum(Jump)#비용 산출

        if Fly_Dis > Jump_dn + Jump: # 이동 조건
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

    