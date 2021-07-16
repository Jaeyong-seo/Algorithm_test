#백준 #2775 #부녀회장이 되고싶어

def address(floors, number):

  for floor in range(0,floors+1):

    #0층 일때 배열 생성
    if floor==0:
      f_array = [i for i in range(1, number+1)]
      print(f_array)
    #1 ~ N층 까지
    else:
      for num in range(1,number):
        f_array[num] = f_array[num-1] + f_array[num]
        print(f_array)

  print(f_array[number-1])

#---------------------------------------------
times = int(input())

for _ in range(times):
  floor = int(input())
  number = int(input())
  address(floor,number)