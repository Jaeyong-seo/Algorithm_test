class PrimeNumber():
    def __init__(self):
        self.PrimeNum_list = []
        self.Divisor_list = []

    def search(self,M,N):
        for num in range(M,N+1):
            self.Divisor_list = []
            for n in range(1,num+1):
                if num % n == 0:
                    self.Divisor_list.append(n)
            if len(self.Divisor_list) == 2:
                self.PrimeNum_list.append(num)
        return self.PrimeNum_list

    def sum(self):
        return sum(self.PrimeNum_list)

    def min(self):
        return min(self.PrimeNum_list)

    def is_empty(self):
        if self.PrimeNum_list:
            return 0
        return 1


M = int(input())
N = int(input())

PrimeNumber().search(M,N)

if PrimeNumber.is_empty():
    print(-1)
else:
    print(PrimeNumber.sum())
    print(PrimeNumber.min())