# 프로그래머스 #K번째수
def solution(a_array, command):
    answer = []

    for com in command:
        start, end, select = com

        answer.append(sorted(a_array[start - 1: end])[select - 1])

    return answer


solution([1, 5, 2, 6, 3, 7, 4], [[2, 5, 3], [4, 4, 1], [1, 7, 3]])