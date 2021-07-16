# 프로그래머스 #예산
def solution(d, budget):
    check = 0
    d_list = sorted(d)

    for idx, value in enumerate(d_list):

        if sum(d_list) < budget:
            idx = len(d_list)

        if check > budget:
            idx -= 1
            break
        check += value

    if check == budget:
        idx += 1

    return idx


solution([1], 9)
# solution([2,2,3,3],10)