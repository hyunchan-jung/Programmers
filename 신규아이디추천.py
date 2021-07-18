import re

def solution(new_id):
    # step 1 : 소문자로 변경
    new_id = new_id.lower()
    
    # step 2 : 영소문자, 숫자, -, _, . 제외한 글자 제거
    new_id = re.sub('[^a-z0-9\-\_\.]', '', new_id)
    
    # step 3 : ..을 .으로 변경
    new_id = re.sub('\.{2,}', '.', new_id)
        
    # step 4 : 양쪽 . 제거
    new_id = new_id.strip('.')
    
    # step 5 : 빈문자 a로 변경
    if new_id == '': new_id = 'a'
        
    # step 6 : 최대길이 15
    new_id = new_id[:15]
    # repeat step 4 : 길이 변경 후 다시 양쪽 . 제거
    new_id = new_id.strip('.')
    
    # step 7 : 길이 2이하일때 길이가 3이될때까지 마지막문자 추가
    while len(new_id) < 3:
        new_id += new_id[-1]
        
    return new_id