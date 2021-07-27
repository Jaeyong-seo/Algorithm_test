def solution(N):
    #N까지 소수 목록 구하기
    check = [True] * (2*N+1)
    cnt = 0

    for i in range(2, int((2*N)**0.5)+1):
        if check[i]:
            for j in range(i+i,2*N+1,i):
                check[j] = False

    #N보다 크고 2N 보다 작은 범위의 True 갯수 반환
    for i in range(N+1,2*N+1):
        if check[i] and i > 1:
            cnt += 1
    return cnt
            
while True:
    N = int(input())
    if N == 0:
        break
    else:
        print(solution(N))
    