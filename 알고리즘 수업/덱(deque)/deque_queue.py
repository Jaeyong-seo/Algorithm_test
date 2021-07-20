from collections import deque

class Queue:
    def __init__(self, n):
        self.array = deque()

    def push(self, num):
        self.array.append(num)

    def pop(self):
        if self.array:
            return self.array.pop()
        return -1

    def size(self):
        return len(self.array)

    def empty(self):
        if self.array:
            return 0
        return -1

    def front(self):
        return self.array[0]

    def back(self):
        return self.array[-1]

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