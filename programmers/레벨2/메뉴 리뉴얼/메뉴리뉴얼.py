from itertools import combinations,permutations
from collections import Counter

def solution(orders, course):
    answer = []


    for i in course:
        all_menus = []
        for order in orders:
            all_menus += [''.join(i) for i in list(combinations(sorted(order),i))]
        food = dict(Counter(all_menus))
        check = sorted(food.items(), key=lambda x: x[1], reverse=True)
        check_a = list(filter(lambda x:x[1]==check[0][1]and x[1] > 1,check))
        [answer.append(i[0]) for i in check_a]


    return sorted(answer)

print(solution(["ABCFG", "AC", "CDE", "ACDE", "BCFG", "ACDEH"],[2,3,4]))
print(solution(["XYZ", "XWY", "WXA"],[2,3,4]))