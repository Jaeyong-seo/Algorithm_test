from collections import deque

class Queue:
    def __init__(self, n):
        self.array = deque()
        self.f_idx = 0
        self.b_idx = 0

    def push(self, num):
        self.array.append(10)
        self.b_idx += 1

    def pop(self):
        last_val = self.array.pop()
        self.b_idx -=1

    def size(self):

    def empty(self):

    def is_empty(self):

    def front(self):

    def back(self):

def run_cmd_with_queue(queue_obj, command):
    cmd_type = command[0]

    if cmd_type == "push":
        _, num = command
        queue_obj.push(int(num))
    elif cmd_type == "pop":
        print(queue_obj.pop())
    elif cmd_type == "size":
        print(queue_obj.size())
    elif cmd_type == "empty":
        print(queue_obj.empty())
    elif cmd_type == "front":
        print(queue_obj.front())
    elif cmd_type == "back":
        print(queue_obj.back())


n = int(input())
queue_obj = Queue(n)

for _ in range(n):
    run_cmd_with_queue(queue_obj, input().split())