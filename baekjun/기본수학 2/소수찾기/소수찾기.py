def PrimeNumber_Cnt(array):
    cnt = 0
    for num in array:
        divisor_list = []
        for n in range(1,num+1):
            if num % n == 0:
                divisor_list.append(n)
        if len(divisor_list) == 2:
           cnt += 1
    return cnt

times = int(input())
num_list = list(map(int,input().split()))
print( PrimeNumber_Cnt( num_list )수