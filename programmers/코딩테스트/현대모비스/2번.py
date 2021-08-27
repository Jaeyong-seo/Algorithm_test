import collections

def solution(a_string):
    answer = []

    #문자열 양 끝에 a가 있으면 쳐내기
    for a in a_string:
        a_cnt = a.count('a')
        while True:
            if len(a) <= 1:
                break
                
            if a[0] == 'b' and a[-1] == 'b':    
                # a_cnt = collections.Counter(a)['a']
                # # a 앞뒤로 a_cnt 갯수만큼 'b'가 있는지 확인해서 맞으면 그만큼 'b' 제거
                # if collections.Counter(a[:a_cnt]) == collections.Counter(a[-a_cnt:]):
                    # a = a[a_cnt:-a_cnt]
                a = a[1:-1]
                continue

            if len(a) <= 1:
                break

            if a[0] == 'a':
                a = a[1:]
                continue
            if a[-1] == 'a':
                a = a[:-1]
                continue
            

        if 'a' == a:
            answer.append(True)
        else:
            answer.append(False)

    return answer


a = ["bab","bbaaaa","bababa","bbbbbbbabababbbaabbbb"]
print(solution(a))