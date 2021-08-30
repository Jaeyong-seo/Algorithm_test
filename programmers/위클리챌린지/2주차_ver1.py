import pandas as pd

LeaderBoard = 'FFFFFDDCBAA'

def solution(N):
    answer = ''
    scores = pd.DataFrame(N)

    for i in range(len(N)):
        if scores[i].max() == scores[i][i] or scores[i].min() == scores[i][i]:
            if list(scores[i]).count(scores[i][i]) == 1:
                scores[i][i] = None

        answer += ( LeaderBoard[int(scores[i].mean())//10] )

    return answer
    

# print(solution([[100,90,98,88,65],[50,45,99,85,77],[47,88,95,80,67],[61,57,100,80,65],[24,90,94,75,65]]))
# print(solution([[50,90],[50,87]]))
print(solution([[70,49,90],[68,50,38],[73,31,100]]))