import sys

def Prime_num(N):
    check = [True] * (N)
    # N까지 소수목록 생성
    for i in range(2, int(N**0.5)+1):
        for j in range(i+i,N,i):
            if check[i]:
                check[j] = False

    return [i for i in range(2,N) if check[i]]

def solution(N):
    Prime = Prime_num(N)
    #골드바흐
    idx = max([i for i in range(len(Prime)) if Prime[i] <= N/2])

    for i in range(idx,-1,-1):
        for j in range(i,len(Prime)):
            if Prime[i] + Prime[j] == N:
                return [Prime[i],Prime[j]]

times = int(sys.stdin.readline())
for _ in range(times):
    N = int(sys.stdin.readline())
    answer = solution(N)
    print(f'{answer[0]} {answer[1]}')

