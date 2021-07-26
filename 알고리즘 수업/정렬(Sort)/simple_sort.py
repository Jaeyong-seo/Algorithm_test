def insertion_sort(arr_copy):
    arr = arr_copy.copy()
    for check in range(len(arr)):
        for ck in range(check,0,-1):
            if arr[ck] < arr[ck-1]:
                arr[ck],arr[ck-1] = arr[ck-1],arr[ck]
    return arr

def selection_sort(arr_copy):
    arr = arr_copy.copy()
    for check in range(len(arr)-1):
        m_val = arr.index(min(arr[check+1:]))
        if arr[check] > arr[m_val]:
            arr[check], arr[m_val] = arr[m_val], arr[check]
    return arr

def bubble_sort(arr_copy):
    arr = arr_copy.copy()
    for check in range(len(arr)-1,0,-1):
        for ck in range(check):
            if arr[ck] > arr[ck+1]:
                arr[ck],arr[ck+1] = arr[ck+1],arr[ck]
    return arr

# n = int(input())
num_list = [5,4,3,2,1]

# for _ in range(n):
#     num = int(input())
#     num_list.append(num)

insertion_sorted_list = insertion_sort( num_list )
print(" ".join(map(str, insertion_sorted_list)))

selection_sorted_list = selection_sort(num_list)
print(" ".join(map(str, selection_sorted_list)))

bubble_sorted_list = bubble_sort(num_list)
print(" ".join(map(str, bubble_sorted_list)))
