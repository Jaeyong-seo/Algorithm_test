class Stack:
    def __init__(self, n):
        self.stack = [None for _ in range(n)]
        self.stack_size = 0
    
    def push(self, num):
        # self.stack.append(int(num))
        self.stack[self.stack_size] = int(num)
        self.stack_size += 1

    def pop(self):
        if self.size() > 0:
            last_val = self.top()
            self.stack[self.stack_size-1] = None
            self.stack_size -= 1
            return last_val
            # return self.stack.pop()
        
        return -1

    def size(self):
        return self.stack_size
    
    def empty(self):
        if self.size() > 0:
            return 0
        
        return 1
        
        # print(int(self.stack_size <= 0))
    
    def top(self):
        if self.size() > 0:
            return self.stack[self.size()-1]
        
        return -1

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
    # "push 2".split(" ") # => ["push", "2"]
    # "size".split(" ") # => ["size"]

    cmd_list = input().split(" ")
    obj_stack = run_with_cmd_stack(obj_stack, cmd_list)
    # print(obj_stack.stack)
    # print(obj_stack.stack_size)

    # if result is not None:
    #     stack = result
