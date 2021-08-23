def solution(card_numbers):
    return [cal_luhn(card_number) for card_number in card_numbers]
    
def cal_luhn(card_number):
    # 만약 신용카드 형식이 아니라면 리턴 0
    # 만약 신용카드 형식이 맞다면 replace('-','') 이후 코드 진행
    for idx in range(len(card_number)):
        even_sum = 0
        odd_sum = 0
        if idx % 2 == 0:
            even_sum += sum([int(i) for i in str(int(card_number[idx]) * 2)])
        else:
            odd_sum += int(card_number[idx])
    return (even_sum + odd_sum) % 10 == 0