
class Circular_Queue:
    def __init__(self,n):
        self.array = [None] * Q_size
        self.front = 0 % Q_size
        self.back = 0 % Q_size


    def enQueue(self, num):
        self.array[self.back] = int(num)
        self.back = (self.back + 1) % Q_size
        print(self.array)
        print(self.back)
        
    
    def deQueue(self):
        last_val = self.array[self.front]
        self.array[self.front] = None
        print(self.array)
        self.front = (self.front + 1) % Q_size
        return last_val
        
    def size(self):
        return abs(self.front - self.back)
    
    def empty(self):
        if self.array:
            return 0
        if self.front == self.back:
            return 1
    
    def front_val(self):
        if self.empty == 1:
            return -1
        return self.array[self.front]
    
    def back_val(self):
        if self.empty == 1:
            return -1
        return self.array[self.back-1]

    

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
    elif cmd_type == "front":
        print(Cqueue_obj.front_val())
    elif cmd_type == "back":
        print(Cqueue_obj.back_val())

Q_size = 6

n = int(input())
Cqueue_obj = Circular_Queue(n)

for _ in range(n):
    run_cmd_with_queue(Cqueue_obj, input().split())