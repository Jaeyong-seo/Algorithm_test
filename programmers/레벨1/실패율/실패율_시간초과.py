# 프로그래머스 #실패율 #시간초과
import operator
def solution(N, stages):
    answer = {}

    for stage in range(1, N + 1):

        not_clear = list(filter(lambda x: x <= stage, stages))  # 클리어 하지 못한 사람
        arrive = list(filter(lambda x: x >= stage, stages))  # 스테이지 도착한 사람

        try:
            answer[stage] = len(not_clear) / len(arrive)  # 실패율구하기
        except:
            answer[stage] = 0

        print('클리어 하지 못한 사람', not_clear)
        print('스테이지에 도달한 사람', arrive)

        stages = [x for x in stages if x not in not_clear]  # 리스트 빼기

        result = sorted(answer.items(), key=operator.itemgetter(1), reverse=True)  # 스테이지별 실패율 정렬

    return [x[0] for x in result]  # 정렬값의 key 반환


print(solution(5, [2, 1, 2, 6, 2, 4, 3, 3]))
