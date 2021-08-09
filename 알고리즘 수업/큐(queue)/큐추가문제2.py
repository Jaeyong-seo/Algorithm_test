from collections import deque

N, M = map(int,input().split())
pop_list = list(map(int,input().split()))

Card_dummy = deque(range(1,N+1))

for find_idx in pop_list:
    num_idx = Card_dummy.index(find_idx)
    move_cnt = num_idx

    if move_cnt > ()