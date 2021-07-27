# [..., 1,2,3,4,5,6,7, ...]

class Circular_Queue:
    def __init__(self, n):
        self.array = [None] * n
        # self.array = [None for _ in range(n)]
        self.front = 0 % n
        self.back = 0 % n


    def enQueue(self, num):
        self.array[self.back] = int(num)
        print(self.array)
        self.back += 1
    
    def deQueue(self):
        self.array[self.back] = None
        print(self.array)
        self.back -= 1
        pass
        
    def size(self):
        pass
    
    def empty(self):
        pass

    
def run_cmd_with_queue(Cqueue_obj, command):
    cmd_type = command[0]
    
    if cmd_type == "enQueue":
        _, num = command
        Cqueue_obj.enQueue(int(num))
    elif cmd_type == "deQueue":
        print(Cqueue_obj.deQueue())
    elif cmd_type == "size":
        print(Cqueue_obj.size())
    elif cmd_type == "empty":
        print(Cqueue_obj.empty())

n = int(input())
Cqueue_obj = Circular_Queue(n)

for _ in range(n):
    run_cmd_with_queue(Cqueue_obj, input().split())



