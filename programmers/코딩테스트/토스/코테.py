
name_list = ["김비바", "김비바", "이비바", "김토스", "이비바", "김비바"]


def solution(name_list):
    answer_list = []
    name_checklist = list(set(name_list))
    dic = {}
    

    for name in name_checklist:
        dic[name] = 0

    for name in name_list:
        val = name + chr(65 + dic[name])
        dic[name] += 1
        answer_list.append(val)
    
    return answer_list
        
