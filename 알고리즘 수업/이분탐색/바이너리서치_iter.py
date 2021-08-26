def binary_search(n_list, target):
    start_idx = 0
    end_idx = len(n_list)-1

    while start_idx <=end_idx:
        mid_idx = (start_idx + end_idx) // 2

        if target < n_list[mid_idx]:
            end_idx = mid_idx
        elif target > n_list[mid_idx]:
            start_idx = mid_idx + 1
        else:
            return mid_idx
    return -1

n = int(input())
num_list = list(map(int,input().split()))
num_list.sort()

m = int(input())
for target_num in map(int,input().split()):
    if binary_search(num_list,target_num) >= 0:
        print('1')
    else:
        print('0')