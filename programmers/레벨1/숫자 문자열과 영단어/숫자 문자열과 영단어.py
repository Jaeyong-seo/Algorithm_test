def solution(SecretCode):
  decoder = {'zero':0,'one':1,'two':2,'three':3,'four':4,'five':5,'six':6,'seven':7,'eight':8,'nine':9}
  answer = []
  S_code = []

  for d in SecretCode:
    if d.isdigit():
      answer.append(d)
    else:
      S_code.append(d)
      decode = ''.join(S_code)

      try: 
        answer.append(str(decoder[decode]))
        S_code = []
      except: pass

  return int(''.join(answer))

print(solution("one4seveneight"))