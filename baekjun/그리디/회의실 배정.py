def solution(meeting):
    now = 0
    cnt = 0
    
    meeting.sort(key=lambda x : x[0])
    meeting.sort(key=lambda x : x[1])

    for meet in meeting:
        if meet[0] >= now:
            print(meet)
            now = meet[1]
            cnt +=1
    return cnt

time = int(input())
meeting = [tuple(map(int,input().split())) for i in range(time)]
print(solution(meeting))



