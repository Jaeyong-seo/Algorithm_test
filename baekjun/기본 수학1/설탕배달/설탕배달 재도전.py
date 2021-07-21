#백준 #설탕배달
def sugar(N):
    if N in [4,7]:#---------------------4,7 예외처리
        return -1
    elif N % 5 == 0:#-------------------5로 나누어 떨어질 때
        return N//5
    else:
        for cnt_5 in range(N//5,0,-1):#--N//5 부터 1까지 -1
            Now = N - (cnt_5*5)
            if Now % 3 == 0:#5로 나누고 나머지가 3으로 나누어떨어진다면
                return cnt_5 + (Now//3)
        return N//3#-------------------3으로 나누어 떨어질 때

N = int(input())
print(sugar(N))