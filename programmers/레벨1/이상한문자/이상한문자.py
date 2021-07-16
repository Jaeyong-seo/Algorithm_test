#프로그래머스 #이상한문자
def solution (n):
  s_cnt = 0
  answer = ''

  for i in n:
    if i == ' ':
      s_cnt = 0
    else:
      s_cnt += 1

    if s_cnt:
      if s_cnt%2 == 1: answer += i.upper()
      else: answer += i.lower()
    else:
      answer += i
  return answer

solution("try hello world")