N = int(input())

stack = list(range(N,0,-1))

cycle = 0
element = 0

while len(stack) > 1:
    stack = stack[:-1]
    element += len(stack)
    stack = [stack[-1]] + stack[:-1]
    element += len(stack)
    cycle += 1
    

print('element',element)
print('cycle',cycle)
print(stack[0])