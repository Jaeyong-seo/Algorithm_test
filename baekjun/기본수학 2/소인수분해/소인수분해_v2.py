def PrimeNum_Next(N):
    number = N+1

    while True:
        for num in range(N+1,number+1):
            Divisor_list = []
            for n in range(1,num+1):
                if num % n == 0:
                    Divisor_list.append(n)
            if len(Divisor_list) == 2:
                return num
        number += 1

def PrimeFactorization(number):
    Factor_list = []
    f_check = 0
    p_check = 2


    Factor_list.append(number)

    while True:
        print(Factor_list[-1])
        if Factor_list[-1]  == p_check:
            break
        else:
            while True:
                #print('list', Factor_list)
                #print('num', f_check)
                A, B = divmod(Factor_list[f_check], p_check)
                #print('A:',A)
                #print('B:',B)
                if B == 0:
                    Factor_list[f_check] = p_check
                    Factor_list.append(A)
                    f_check += 1
                    break
                else:
                    p_check = PrimeNum_Next(p_check)
    return Factor_list


N = int(input())

answer = PrimeFactorization(N)
for i in answer:
   print(i)