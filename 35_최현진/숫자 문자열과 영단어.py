def solution(s):
    answer = 0
    num_list = ['zero', 'one', 'two', 'three', 'four',
                'five', 'six', 'seven', 'eight', 'nine']

    for i, num in enumerate(num_list):
        n = str(i)
        s = s.replace(num, n)
    answer = int(s)

    return answer
