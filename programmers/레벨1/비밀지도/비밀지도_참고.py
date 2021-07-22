from Tools.demo.spreadsheet import rjust


def solution(n, arr1, arr2):
    answer = []

    for one,two in zip(arr1,arr2):
        K = str(bin(one | two)[2:])
        K = rjust(n,'0')
        K = K.replace('1','#')
        K = K.replace('0',' ')
        answer.append(K)

    return answer

print(solution(5,[9, 20, 28, 18, 11],[30, 1, 21, 17, 28]))