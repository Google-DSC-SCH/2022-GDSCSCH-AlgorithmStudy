#https://school.programmers.co.kr/learn/courses/30/lessons/72410
import re 

def solution(new_id):
    #1st #2nd #3rd #4th
    new_id = re.sub(r"\.+",".",re.sub('[^a-z0-9_.-]',"",new_id.lower())).strip('.').strip()
    #5th
    if new_id == "": new_id = 'a'
    #6th
    new_id = new_id[:15].rstrip('.')
    #7th
    while len(new_id) <= 2:
        new_id+=(new_id[-1:])
    answer = new_id
    return answer