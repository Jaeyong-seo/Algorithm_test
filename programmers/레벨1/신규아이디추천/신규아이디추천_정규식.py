#프로그래머스 #신규아이디추천 #정규표현식
import re

def solution(id):
  #1단계
  id = id.lower()

  #2단계
  id = re.sub('[^a-z0-9\-_.]','', id)

  #3단계
  id = re.sub('\.+','.',id)

  #4단계
  id = id.strip('.')

  #5단계,6단계 (글자길이 0 일때 a 삽입 및 글자수 15글자 제한)
  id = 'a' if len(id) == 0 else id[:15]

  #6단계( 끝 마침표(.)제거 )
  id = id.strip('.')

  #7단계
  while len(id) < 3 : id += id[-1]

  return id

solution("....!@BaT#*..y.abcdefghijDDDDklm")