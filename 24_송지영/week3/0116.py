#신규 아이디 추천
#https://school.programmers.co.kr/learn/courses/30/lessons/72410

import re

def solution(new_id):
    #1
    new_id = new_id.lower()
    #2
    new_id = re.sub(r"[^a-z0-9\-\_\.]", "", new_id)
    #3
    while '..' in new_id:
        new_id = new_id.replace('..', '.')
    #4
    new_id = new_id.strip('.')
    #5
    if new_id == '':
        new_id = 'a'
    #6
    if len(new_id) >= 16:
        new_id = new_id[:15]
        if new_id[-1] == '.':
            new_id = new_id[:14]
    #7
    while len(new_id) < 3:
        new_id += new_id[-1]
    return new_id