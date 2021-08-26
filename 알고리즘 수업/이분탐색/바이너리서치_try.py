
def num_search(dummy, Number):
    check_point = len(dummy)//2

    if dummy[0] == Number:
        return 1
    
    if dummy[check_point] > Number:
        if len(dummy) > 1:
            return num_search(dummy[:check_point],Number)
        else:
            return 0
    else:
        if len(dummy) > 1:
            return num_search(dummy[check_point:],Number)
        else:
            return 0
            


N = int(input())
dummy = list(map(int,input().split(' ')))
M = int(input())
answer = list(map(int,input().split(' ')))

dummy.sort()

for i in answer:
    print(num_search(dummy,i))