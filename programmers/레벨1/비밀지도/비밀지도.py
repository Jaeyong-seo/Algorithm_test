def Change_two(idx,num):
    value = format(num,'#b')[2:]
    return f'{"0" * (idx - len(value))}{value}'

def Binary_Sum(n,num1,num2):
    b_num1 = Change_two(n,num1)
    b_num2 = Change_two(n,num2)
    b_sum = []

    for i in range(n):
        b_sum.append( int(b_num1[i]) | int(b_num2[i]) )

    return ''.join(map(str,b_sum))

def mosaic(n):
    n = n.replace('1','#')
    n = n.replace('0',' ')
    return n

def solution(n, arr1, arr2):
    answer = []
    for area in range(n):
            answer.append( mosaic( Binary_Sum( n,arr1[area], arr2[area] ) ) )
    return answer

print(solution(5,[9, 20, 28, 18, 11],[30, 1, 21, 17, 28]))