def solution(price, money, count):

    check = 0

    for i in range(1,count+1):
        check += price * i

    answer  = check - money
    if answer > 0:
        return check - money
    else:
        return 0

print(solution(3,20,1))