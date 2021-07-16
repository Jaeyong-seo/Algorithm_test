#프로그래머스 #키패드 누르기
key_pad = ['*','7','4','1','0','8','5','2','#','9','6','3']#---(0,0)= *

def search(n):#------------------------좌표평면 호출 함수(X,Y)
  return key_pad.index(n)//4, key_pad.index(n)%4

def gap(a1, a2):#----------------------두 좌표 거리 호출 함수
  return (abs(a1[0]-a2[0]) + abs(a1[1]-a2[1]))

def solution(numbers, hand):

  left_hand = (0,0)
  right_hand = (2,0)
  answer = ''

  for num in numbers:
    result = search(str(num))#-----------키패드에서 (X,Y)를 탐색해서 result에 저장

    if result[0] == 0:#------------------X축이 0일때(*,7,4,1) L값 추가 / 왼손 현위치 저장
      answer += 'L'
      left_hand = result

    elif result[0] == 2:#------------------X축이 2일때(#,9,6,3) R값 추가 / 오른손 현위치 저장
      answer += 'R'
      right_hand = result

    elif result[0] == 1:#------------------X축이 1일때(0,8,5,2)
      left_gap = gap(left_hand,result)#-----gap함수 이용 거리저장
      right_gap = gap(right_hand,result)

      if left_gap == right_gap:#----------거리 같을 때 왼손/오른손 잡이 판별
        if hand == 'right':
          answer += 'R'
          right_hand = result
        else:
          answer += 'L'
          left_hand = result
      elif left_gap < right_gap:#-------왼손이 가까울 때
        answer += 'L'
        left_hand = result
      elif right_gap < left_gap:#-------오른손이 가까울 때
        answer += 'R'
        right_hand = result

  return answer


# solution([1, 3, 4, 5, 8, 2, 1, 4, 5, 9, 5],"right")
# solution([7, 0, 8, 2, 8, 3, 1, 5, 7, 6, 2],"left")
solution([1, 2, 3, 4, 5, 6, 7, 8, 9, 0], "right")