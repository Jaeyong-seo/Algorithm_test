from collections import deque

N = int(input())

card_dummy = deque(list(range(1,N+1)))

while len(card_dummy) > 1:
    card_dummy.popleft()
    card_dummy.rotate(-1)
print(card_dummy[0])
