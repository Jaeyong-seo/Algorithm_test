# 백준 #2775 #부녀회장

def address(floors, number):
    apt = []

    for floor in range(floors + 1):
        floor_array = []
        A = 1

        for num in range(1, number + 1):
            if floor == 0:
                floor_array.append(num)
            else:
                floor_array.append(A)
                try:
                    A += apt[floor - 1][num]
                except:
                    pass

        apt.append(floor_array)

    print(apt[floors][number - 1])


times = int(input())

for _ in range(times):
    floor = int(input())
    number = int(input())

    address(floor, number)