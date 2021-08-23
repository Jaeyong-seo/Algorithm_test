def solution(arr):
    arr.sort()
    check = len(arr)

    for val in arr:
        a = len(arr) - len([i for i in arr if i > val])
        b = len(arr) - a
        v = abs(a-b)
        
        if v < check:
            check=v
            answer = val
    return answer +1
        

# arr = [1,52,125,10,25,201,244,192,128,23,203,98,154,255]
# arr = [0,0,255,255,0,0,255,255,255]
arr = [100,100,100]
print(solution(arr))