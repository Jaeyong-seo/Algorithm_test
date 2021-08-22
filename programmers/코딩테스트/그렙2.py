

def solution(card_numbers):
    #신용카드 번호 전처리
    numbers = [i.replace('-','',4) for i in card_numbers]

    #Luhn공식 구현
    answer = []
    for number in numbers:
        for idx, num in enumerate(number):
            arr1 = []
            arr2 = []

            if idx % 2 == 0:
                val = int(num)*2
                if val < 10:
                    arr1.append(val)
                else:
                    arr1.append(str(val)[0]+str(val)[1])
            else:
                arr2.append(val)

            try:
                if sum(arr1) % sum(arr2)==0:
                    answer.append(1)
                else:
                    answer.append(0)
            except:
                pass
    return answer

            



    

    return numbers


arr = ["3285-3764-9934-2453", "3285376499342453", "3285-3764-99342453", "328537649934245", "3285376499342459", "3285-3764-9934-2452"]
print(solution(arr))