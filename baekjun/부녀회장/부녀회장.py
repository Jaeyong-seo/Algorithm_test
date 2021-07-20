# 백준 #2775 #부녀회장
def address(floors, number):
    apt = []#--------------------------------2차원 배열 저장
    for floor in range(floors + 1):#---------floor 현재층
        floor_array = []#--------------------각 층마다 배열을 저장할 1차원 배열
        A = 1#-------------------------------각 층의 1호는 1명
        for num in range(1, number + 1):
            if floor == 0:#------------------0층 [0,1,2,3,....,N] 생성
                floor_array.append(num)
            else:
                floor_array.append(A)
                try:
                    A += apt[floor - 1][num]#-아래층 [N] 번째 숫자 불러와 누적
                except:
                    pass
        apt.append(floor_array)
    print(apt[floors][number - 1])#----------구하려는 목적 위치 값 출력

times = int(input())
for _ in range(times):
    floor = int(input())
    number = int(input())
    address(floor, number)