#프로그래머스 #3진법
def solution(number):
  three = ""
  cycle = 0

  while number > 0:
    a1,a2 = divmod(number,3)
    number = a1
    three += str(a2)

  return int(three,3)

solution(45)