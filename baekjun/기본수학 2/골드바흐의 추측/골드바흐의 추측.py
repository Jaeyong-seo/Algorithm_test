import sys

def solution(N):
    check = [True] * (N+1)
    Prime = []
    
    # N까지 소수목록 생성
    for i in range(2, N):
        for j in range(i+i,N,i):
            if check[i]:
                check[j] = False

    for i in range(2,N):
        if check[i]:
            Prime.append(i)
    #골드바흐
    for i in range(len(Prime)-1,-1,-1):
        for j in range(len(Prime)-1,-1,-1):
            if Prime[i] == N - Prime[j] and i < j: 
                return [Prime[i], Prime[j]]



times = int(sys.stdin.readline())
for _ in range(times):
    N = int(sys.stdin.readline())
    answer = solution(N)
    print(f'{answer[0]} {answer[1]}')
