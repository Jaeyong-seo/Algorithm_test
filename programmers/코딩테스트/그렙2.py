# Luhn공식 구현
def Luhn(N):
    case_1 = 0
    case_2 = 0

    for idx,val in enumerate(N):
        val = int(val)

        if idx % 2 == 0:
            val = val*2
            if val < 10:
                case_1 += val
            else:
                val = int(str(val)[0]) + int(str(val)[1])
                case_1 += val
        else:
            case_2 += val

    if (case_1 + case_2) % 10 == 0:
        return 1
    else:
        return 0

def solution(card_numbers):
    #신용카드 번호 전처리
    numbers = [i.replace('-','',4) for i in card_numbers]
    answer = []
    
    for number in numbers:
        answer.append(Luhn(number))

    return answer

arr = ["3285-3764-9934-2453", "3285376499342453", "3285-3764-99342453", "328537649934245", "3285376499342459", "3285-3764-9934-2452"]
print(solution(arr))
