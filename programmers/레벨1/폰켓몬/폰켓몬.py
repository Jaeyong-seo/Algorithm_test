def solution(nums):

    A = len(set(nums))
    B = int(len(nums) / 2)

    return min(A,B)

print(solution([3,1,2,3]))