from collections import deque
#Stack
class Stack:
    def __init__(self, n):
        self.stack = deque()
        self.stack_size = 0

    def push(self, num):
        self.stack.append(num)
        self.stack_size += 1
    def pop(self):
        if self.stack_size:
            last_val = self.stack.pop()
            self.stack_size -= 1
            return last_val
        return -1
    def size(self):
        return self.stack_size
    def empty(self):
        if self.stack_size:
            return 0
        return -1
    def top(self):
        return self.stack[ self.stack_size-1 ]

def run_with_cmd_stack(obj_stack, cmd_list):
    cmd_type = cmd_list[0]

    if cmd_type == "push":
        _, num = cmd_list
        obj_stack.push(num)
    elif cmd_type == "pop":
        print(obj_stack.pop())
    elif cmd_type == "size":
        print(obj_stack.size())
    elif cmd_type == "empty":
        print(obj_stack.empty())
    elif cmd_type == "top":
        print(obj_stack.top())

    return obj_stack


n = int(input())
obj_stack = Stack(n)

for _ in range(n):

    cmd_list = input().split(" ")
    obj_stack = run_with_cmd_stack(obj_stack, cmd_list)

