# 프로그래머스 #신규아이디추천
def solution(new_id):
    rule = '.-_'
    new_answer = ''

    # 대문자 -> 소문자 치환
    answer = new_id.lower()

    # 조건에 부합하지 않는 문자 제거
    for value in answer:
        if value.isalpha() or value.isdigit() or (value in rule):
            new_answer += value
    answer = new_answer

    # 마침표(.)가 연속으로 등장한 부분 마침표(.)한개로 변환
    while '..' in answer:
        answer = answer.replace('..', '.')

    # 마침표(.)위치가 처음이나 끝 이라면 제거
    if len(answer) > 2:
        if answer[0] == '.':
            answer = answer[1:]
        if answer[-1] == '.':
            answer = answer[:-1]
    else:
        if answer[0] == '.':
            answer = ''

    # new_id의 길이가 16이상이라면 앞에서부터 15글자 제외한 문자를 제거
    if len(answer) >= 16:
        answer = answer[:15]

    # new_id가 빈 문자열이라면 'a' 대입.
    if len(answer) == 0:
        answer = 'a'

    # 제거후 마지막 글자가 마침표(.)라면 제거
    if answer[-1] == '.':
        answer = answer[:-1]

    # new_id의 길이가 2글자 이하라면 new_id의 마지막 문자를 길이가 3이 될때까지 붙여준다
    while len(answer) < 3:
        answer += answer[-1]

    return answer


solution("....!@BaT#*..y.abcdefghijDDDDklm")
