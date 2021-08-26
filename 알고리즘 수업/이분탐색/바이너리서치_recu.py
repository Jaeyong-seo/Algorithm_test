def binary_search(n_list,target,start_idx,end_idx):
    mid_idx = (start_idx + end_idx) // 2

    if n_list[mid_idx] == target:
        return 1
    
    if len(n_list) > 1:
        if target > n_list[mid_idx]:
            start_idx = mid_idx + 1 
        else:
            end_idx = mid_idx
        return binary_search(n_list,target,start_idx,end_idx)
    else:
        return 0

n = int(input())
n_list = list(map(int,input().split()))

m = int(input())

for target in map(int,input().split()):
    print(binary_search(n_list,target,0,(m-1)))