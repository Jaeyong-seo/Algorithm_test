def Prime(N):
  answer = []
  check = [True] * (N+1)

  for i in range(2, int(N**0.5)+1):
    if check[i]:
      for j in range(i+i,N+1,i):
        check[j] = False

  for i in range(2,len(check)):
    if check[i]:
      answer.append(i)

  return answer


def PrimeNumFactorization(N):
  PrimeNum_list = []
  answer_list = []

  #N까지 소수 목록 구하기
  PrimeNum_list = Prime(N)

  #소수 목록중 작은 수 부터 N을 나누기
  idx = 0
  while N not in PrimeNum_list:
    # A, B = divmod(N,PrimeNum_list[idx])
    if N % PrimeNum_list[idx] == 0:
      N = N / PrimeNum_list[idx]
      answer_list.append(PrimeNum_list[idx])
    else:
      idx += 1

  #나누어진 수는 정답 리스트에 저장
  answer_list.append(int(N))

  return answer_list

N = int(input())
if N == 1:
  pass
else:
  #오름차순으로 출력
  for i in PrimeNumFactorization(N):
    print(i)
