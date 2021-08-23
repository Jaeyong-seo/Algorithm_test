foods = [300, 130, 120, 20]
foods_limit = [10,30,20,30]

def solution(seconds):
    cnt = 0

    for food,limit in zip(foods,foods_limit):
        A,B = divmod(seconds,food)

        if A <= limit:
            cnt += A
            seconds = B
        else:
            cnt += limit
            seconds = seconds % limit

        if B == 0:
            return cnt

    return cnt


print(solution(3020))