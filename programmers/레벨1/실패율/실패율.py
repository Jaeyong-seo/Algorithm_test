# 프로그래머스 #실패율
import operator

def solution(N, stages):
    answer = {}

    for stage in range(1, N + 1):

        not_clear = 0
        arrive = 0

        for value in stages:
            if (stage - 1) < value <= stage:
                not_clear += 1
            if value >= stage:
                arrive += 1

        try:
            answer[stage] = not_clear / arrive  # 실패율구하기
        except:
            answer[stage] = 0

        # 스테이지별 실패율 정렬 방법
        # result = sorted(answer.items(), key=operator.itemgetter(1),reverse=True)
        result = sorted(answer, key=lambda x: answer[x], reverse=True)
        # result = sorted(answer, key= answer.get,reverse= True)

    return result  # 정렬값의 key 반환


print(solution(5, [2, 1, 2, 6, 2, 4, 3, 3]))