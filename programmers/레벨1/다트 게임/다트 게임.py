def solution(dartResult):
    answer = list(dartResult.replace('*','* ').replace('#','# ').replace('T','T ').replace('D','D ').replace('S','S ').split())

    for dart in answer:


    return answer

print(solution('1S#2D*3T'))