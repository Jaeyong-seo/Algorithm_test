def Prime(M,N):
  check = [True] * (N+1)

  for i in range(2, int(N**0.5)+1):
    if check[i]:
      for j in range(i+i,N+1,i):
        check[j] = False

  for i in range(2,len(check)):
    if check[i] and i >= M :
      print(i)

M,N = map(int,input().split())

Prime(M,N)