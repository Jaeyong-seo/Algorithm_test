def solution(N):
    answer = 0

    for c in coin:
        A,B = divmod(N,c)
        answer += A
        N = B
        
    return answer 

time, money = map(int,input().split())
coin = [int(input()) for c in range(time)][::-1]
print(solution(money))