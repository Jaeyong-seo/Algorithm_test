def FlyToCentauri(X,Y):
    Fly_Dis = Y - X
    cnt = 0  # 이동 횟수
    Jump = 1  # cnt별 이동 가능한 거리
    Jump_sum = 0  # 이동한 거리의 합

    while Jump_sum < Fly_Dis :
        cnt += 1
        Jump_sum += Jump  # cnt 수에 해당하는 move를 더함
        if cnt % 2 == 0 :  # cnt가 2의 배수일 때, 
            Jump += 1  
    return cnt


N = int(input())
for _ in range(N):
    X, Y = map(int,input().split())
    print(FlyToCentauri(X,Y))

