# 프로그래머스 #로또의 최고순위와 최저순위
def solution(lottos, win_nums):
    score = [6, 6, 5, 4, 3, 2, 1]

    lotto_cnt = 0
    zero_cnt = lottos.count(0)

    for num in lottos:
        if num in win_nums:
            lotto_cnt += 1

    return [score[lotto_cnt + zero_cnt], score[lotto_cnt]]


solution([0, 0, 0, 0, 0, 0], [31, 10, 45, 1, 6, 19])