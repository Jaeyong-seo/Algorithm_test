while True:
    num_list = list(map(int,input().split()))

    if sum(num_list) == 0:
        break

    num_list.sort()

    C = num_list[-1] ** 2
    AB = sum(map(lambda x:x**2,num_list[:2]))

    if AB == C:
        print('right')
    else:
        print('wrong')

