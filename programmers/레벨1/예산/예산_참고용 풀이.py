#프로그래머스 #예산 # 눈물 똑똑 ㅠㅜ
def solution(d, budget):
  d.sort()

  while budget > sum(d):
    d.pop()

  return len(d)

solution([2,2,3,3],10)