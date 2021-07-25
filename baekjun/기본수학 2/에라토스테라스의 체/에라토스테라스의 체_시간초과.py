#에라토스테라스의 체
def solution(M,N):
  answer = []
  # check = [i for i in range(2, N+1)]
  check = list(range(2,N+1))
  
  for _ in range(int(N **0.5)):
    answer.append(check[0])
    check = [i for i in filter(lambda x : x % check[0], check)]
  

  for idx,val in enumerate(answer): 
    if val >= M:
      answer = answer[idx:] + check
      break

  for i in answer:
    print(i)


M, N = map(int, input().split())

solution(M,N)