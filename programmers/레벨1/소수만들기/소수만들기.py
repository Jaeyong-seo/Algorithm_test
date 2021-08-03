from itertools import combinations

def solution(nums):
    cnt = 0
    #입력 리스트에서 3개씩 그룹화
    dummy = list(combinations(nums,3))
    #해당 그룹합이 소수인지 아닌지 판별
    for num in dummy:
        N = sum(num)
        for i in range(2, N):
            if N % i == 0:
                break
        else:
            cnt += 1
    return cnt

print(solution([1,2,7,6,4]))