def solution(dartResult):
    score = [0]
    # ['1S', '#', '2D', '*', '3T'] 문자열 변환
    dartgame = list(dartResult.replace('*','* ').replace('#','# ').replace('T','T ').replace('D','D ').replace('S','S ').split())

    for dart in dartgame:
        # print(score)
        #점수다트
        if len(dart) > 1:
            point, area = int(dart[:-1]),dart[-1]
            if area == 'S':
                score.append(point)
            elif area == 'D':
                score.append(point ** 2)
            elif area == 'T':
                score.append(point ** 3)
        #스타상, 아차상
        else:
            if dart == '*':
                score[-1] = score[-1] * 2
                if len(score) > 1:
                    score[-2] = score[-2] * 2
            elif dart == '#':
                score[-1] = -(score[-1])

    return sum(score)

print(solution(' 1S**2T*3S '))
