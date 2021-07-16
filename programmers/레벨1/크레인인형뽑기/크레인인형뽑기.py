#프로그래머스 #크레인인형뽑기게임

def solution(board, moves):
  basket = []
  cnt = 0

  for pick in moves:#-----------------move에 담긴 value 가져옴
        for area in board:#-----------board 가로줄 스캔

        if area[pick-1] != 0:#--------해당 가로줄의 pick-1 번째가 0이 아닐 경우
          basket.append(area[pick-1])#[pick-1]인형 stack에 넣고 인형 0으로 바꿈
          area[pick-1] = 0

        if len(basket) > 1:#----------stack길이가 1이상 일때 같은 인형 삭제
          if basket[-1] == basket[-2]:
            cnt += 2#-----------------인형은 2개씩 터짐
            del basket[-2:]#----------끝에서 2개 삭제
        break

  return cnt

solution([[0, 0, 1, 0, 0],
          [0, 0, 1, 0, 0],
          [0, 2, 1, 0, 0],
          [0, 2, 1, 0, 0],
          [0, 2, 1, 0, 0]],
          [1, 2, 3, 3, 2, 3, 1]
          )