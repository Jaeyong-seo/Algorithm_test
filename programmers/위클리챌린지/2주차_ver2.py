import numpy as np
import collections 

cnt = collections.Counter
LeaderBoard = 'FFFFFDDCBAA'

def solution(scores):
    answer = ''
    scores = np.array(scores)
    
    for idx,score in enumerate(scores):
        if score.max() == score[idx] or score.min() == score[idx]:
            if list(score).count(score[idx]):
            # if cnt(score)[score[idx]]:
                score = np.array(score)
                score[idx] = None
        answer += LeaderBoard[ score.mean()//10 ]
    # for i in range(len(scores)):
    #     if max(scores[i]) == scores[i][i] or max(scores[i]) == scores[i][i]:
    #         if scores[i].count(scores[i][i]):
    #             scores[i][i]=None
    #     print(scores[i])
        
    return answer

print(solution([[100,90,98,88,65],[50,45,99,85,77],[47,88,95,80,67],[61,57,100,80,65],[24,90,94,75,65]]))