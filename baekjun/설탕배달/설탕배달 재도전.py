def sugar(N):
    if N in [4,7]:
        return -1
    elif N % 5 == 0:
        return N//5
    else:
        for cnt_5 in range(N//5,0,-1):
            Now = N - (cnt_5*5)
            if Now % 3 == 0:
                return cnt_5 + (Now//3)
        return N//3

#while True:
N = int(input())
print(sugar(N))