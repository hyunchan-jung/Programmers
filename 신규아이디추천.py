import re

def solution(new_id):
    # step 1 : �ҹ��ڷ� ����
    new_id = new_id.lower()
    
    # step 2 : ���ҹ���, ����, -, _, . ������ ���� ����
    new_id = re.sub('[^a-z0-9\-\_\.]', '', new_id)
    
    # step 3 : ..�� .���� ����
    new_id = re.sub('\.{2,}', '.', new_id)
        
    # step 4 : ���� . ����
    new_id = new_id.strip('.')
    
    # step 5 : ���� a�� ����
    if new_id == '': new_id = 'a'
        
    # step 6 : �ִ���� 15
    new_id = new_id[:15]
    # repeat step 4 : ���� ���� �� �ٽ� ���� . ����
    new_id = new_id.strip('.')
    
    # step 7 : ���� 2�����϶� ���̰� 3�̵ɶ����� ���������� �߰�
    while len(new_id) < 3:
        new_id += new_id[-1]
        
    return new_id