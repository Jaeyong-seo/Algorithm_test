#프로그래머스 #K번째수 #lambda함수
def solution(array,command):
  return list(map(lambda x:sorted(array[x[0]-1 : x[1]])[x[2]-1], command))

solution([1, 5, 2, 6, 3, 7, 4],[[2, 5, 3], [4, 4, 1], [1, 7, 3]])