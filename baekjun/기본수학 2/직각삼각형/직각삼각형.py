while True:
    num_list = list(map(int,input().split()))

    if sum(num_list) == 0:
        break

    C = num_list.pop(num_list.index(max(num_list)))
    AB = sum(map(lambda x:x**2,num_list))

    if AB == (C**2):
        print('right')
    else:
        print('wrong')

