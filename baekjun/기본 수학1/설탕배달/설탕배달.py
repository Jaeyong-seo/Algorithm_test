def sugar(N):
    if N in [4,7]:
        return(-1)
    elif N%5 == 0:
        return(N//5)
    else:
        for cnt_5 in range(N//5,0,-1):
            i,j =  divmod(N,cnt_5*5)
            if j%3==0:
                return( i,)
            now = N % (cnt_5*5)
            if now % 3 == 0:
               return(cnt_5 + now//3)
        return(N//3)

N = int(input())
print(sugar(N))
