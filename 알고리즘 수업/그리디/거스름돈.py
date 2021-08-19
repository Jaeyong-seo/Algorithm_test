
def solution(N):
    answer = 0
    coin = [500,100,50,10,5,1]

    for c in coin:
        A,B = divmod(N,c)
        answer += A
        N = B

    return answer 

print(solution(1000))