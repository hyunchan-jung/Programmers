def solution(a, b):
    answer = 0
    for a, b in zip(a, b): # �� ����Ʈ�� ��Ҹ� ���ؼ� ���信 ����
        answer += (a*b)
    return answer