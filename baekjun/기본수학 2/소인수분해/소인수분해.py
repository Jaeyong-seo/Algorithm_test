from BJ_PrimeNumber import PrimeNumber

class PrimeFactorization(PrimeNumber):
    def __init__(self):
        super().__init__()
        self.Factor_list = []
        self.f_check = 0
        self.p_check = 0


    def Factorization(self,number):
        self.Factor_list.append(number)

        while True:
            if self.Factor_list[self.f_check] in self.PrimeNum_list:
                break
            else:
                while True:
                    A, B = divmod(self.Factor_list[self.f_check],self.PrimeNum_list[self.p_check])
                    if B == 0:
                        self.Factor_list[self.f_check] = self.PrimeNum_list[self.p_check]
                        self.Factor_list.append(A)
                        self.f_check += 1
                        break
                    else:
                        self.p_check += 1

        return self.Factor_list



N = int(input())

PrimeFactorization = PrimeFactorization()
PrimeFactorization.search(0,N)

answer = PrimeFactorization.Factorization(N)
for i in answer:
    print(i)