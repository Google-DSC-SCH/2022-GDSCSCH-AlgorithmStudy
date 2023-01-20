def solution(new_id):
    answer = ''
    special_letters = "~!@#$%^&*()=+[{]}:?,<>/"

    answer = new_id.lower()  # 1단계

    for i in special_letters:
        answer = answer.replace(i, "")  # 2단계

    while '..' in answer:  # 3단계
        answer = answer.replace('..', '.')

    answer = answer.strip('.')  # 4단계

    if answer == "":  # 5단계
        answer = "a"

    if len(answer) > 15:  # 6단계
        answer = answer[:15].strip(".")

    while len(answer) < 3:  # 7단계
        answer += answer[-1]

    return answer
