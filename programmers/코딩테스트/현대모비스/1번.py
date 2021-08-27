from itertools import product

def solution(dices):
    dummy = []

    for i in product(*dices):
        print(i)
        if len(dices) == 1:
            dummy.append(int(f'{i[0]}'))
        elif len(dices) == 2:
            dummy.append(int(f'{i[0]}'))
            dummy.append(int(f'{i[1]}'))
            dummy.append(int(f'{i[0]}{i[1]}'))
            dummy.append(int(f'{i[1]}{i[0]}'))
        elif len(dices) == 3:
            dummy.append(int(f'{i[0]}'))
            dummy.append(int(f'{i[1]}'))
            dummy.append(int(f'{i[2]}'))
            dummy.append(int(f'{i[0]}{i[1]}'))
            dummy.append(int(f'{i[0]}{i[2]}'))
            dummy.append(int(f'{i[1]}{i[0]}'))
            dummy.append(int(f'{i[1]}{i[2]}'))
            dummy.append(int(f'{i[2]}{i[0]}'))
            dummy.append(int(f'{i[2]}{i[1]}'))
            dummy.append(int(f'{i[0]}{i[1]}{i[2]}'))
            dummy.append(int(f'{i[0]}{i[2]}{i[1]}'))
            dummy.append(int(f'{i[1]}{i[0]}{i[2]}'))
            dummy.append(int(f'{i[1]}{i[2]}{i[0]}'))
            dummy.append(int(f'{i[2]}{i[1]}{i[0]}'))
            dummy.append(int(f'{i[2]}{i[0]}{i[1]}'))
            
    dummy = sorted(list(set(dummy)))
    print(dummy)
    for idx,val in enumerate(dummy):
        if val != idx:
            return idx

# dice = [[1, 6, 2, 5, 3, 4], [9, 9, 1, 0, 7, 8]]
dice = [[0, 1, 5, 3, 9, 2], [2, 1, 0, 4, 8, 7], [6, 3, 4, 7, 6, 5]]
print(solution(dice))