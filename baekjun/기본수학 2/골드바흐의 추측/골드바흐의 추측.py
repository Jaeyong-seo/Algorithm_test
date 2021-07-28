import math

def solution(N):
    check = [True] * (N+1)
    Prime = []

    # N까지 소수목록 생성
    for i in range(2, N+1):
        for j in range(i+i,N+1,i):
            if check[i]:
                check[j] = False

    for i in range(2,N+1):
        if check[i]:
            Prime.append(i)
    
    #골드바흐
    point = math.ceil((len(Prime)-1) ** 0.5)

    for i in range(point,-1,-1):
        for j in range(len(Prime)-1,0,-1):
            if Prime[j] + Prime[i] == N:
                if i < j:
                    return [Prime[i], Prime[j]]
                else:
                    return [Prime[j], Prime[i]]

import sys

times = int(sys.stdin.readline())
for _ in range(times):
    N = int(sys.stdin.readline())
    print(' '.join(map(str,solution(N))))
    # print(f'{min(solution(N))} {max(solution(N))}')
