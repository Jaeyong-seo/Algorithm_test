def insertion_sort(arr):
    num = 0
    for idx in range(len(arr)-1):
        if arr[idx] > arr[idx+1]:
            num = arr[idx]
            arr[idx] = arr[idx+1]
            arr[idx + 1] = num
    return arr

def selection_sort():

    return []

def bubble_sort():

    return []

n = int(input())
num_list = []

for _ in range(n):
    num = int(input())
    num_list.append(num)

insertion_sorted_list = insertion_sort( num_list )
print(" ".join(map(str, insertion_sorted_list)))

# selection_sorted_list = selection_sort()
# print(" ".join(map(str, selection_sorted_list)))

# bubble_sorted_list = bubble_sort()
# print(" ".join(map(str, bubble_sorted_list)))
