from itertools import combinations

def solution(p, q):
    answer = []
    idx = 0

    #p,q 비교해서 중복값 제거
    for q_val,p_val in zip(q,p):
        c_check = []
        
        for q_value in q_val:
            if q_value in p_val:
                q_val.remove(q_value)
                p_val.remove(q_value)

        check = [ i for i in combinations(p[idx],2) if sum(i) in q[idx]]

        print(check)

        for i in check:
            q[idx].remove(sum(i))
            p[idx].remove(i[0])
            p[idx].remove(i[1])
            

        if q[idx] or p[idx]:
            answer.append(False)
        else:
            answer.append(True)
        idx += 1

    return answer


p = [[5,3,2,2,1]]
q = [[7,2,4]]

# p = [[5,3,2,1]]
# q = [[7,4]]


# p =[[4,3,3],[1,2,3],[3,2,4]]
# q = [[5,5],[5,1],[1,8]]

print(solution(p,q))