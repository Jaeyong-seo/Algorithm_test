N = int(input())

stack = list(range(N,0,-1))


while len(stack) > 1:
    stack = stack[:-1]
    stack = [stack[-1]] + stack[:-1]
    print(stack)
    

print(stack[0])

#시간 복잡도 O(N**2) 이므로 탈락!8
