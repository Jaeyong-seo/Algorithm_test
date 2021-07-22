def insertion_sort(arr):
    for check in range(len(arr)):
        for idx in range(check,0,-1):
            if arr[idx] < arr[idx-1]:
                num = arr[idx]
                arr[idx] = arr[idx -1]
                arr[idx-1] = num
    return arr

def selection_sort(arr):
    for check in range(len(arr)-1):
        num = arr[check]
        min_num_idx = arr.index(min(arr[check:]))
        arr[check] = arr[min_num_idx]
        arr[min_num_idx] = num
    return arr

def bubble_sort(arr):
    for check in range(len(arr)-1,0,-1):
        for idx in range(check):
            if arr[idx] > arr[idx+1]:
                num = arr[idx]
                arr[idx] = arr[idx+1]
                arr[idx+1] = num
    return arr

n = int(input())
num_list = []

for _ in range(n):
    num = int(input())
    num_list.append(num)

insertion_sorted_list = insertion_sort( num_list )
print(" ".join(map(str, insertion_sorted_list)))

selection_sorted_list = selection_sort(num_list)
print(" ".join(map(str, selection_sorted_list)))

bubble_sorted_list = bubble_sort(num_list)
print(" ".join(map(str, bubble_sorted_list)))
