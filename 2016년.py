# -*- coding: cp949 -*-
def solution(a, b):  # a,b���� ��, ���� �Է¹޴´�.

    day = ['SUN', 'MON', 'TUE', 'WED', 'THU', 'FRI', 'SAT'] # ���� ����
    mon_max = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31] # �� ���� ��������¥
    
    A = sum(mon_max[:a-1]) # 1�� : 1~31, 2�� : 32~  �� ���� ��� ����
    B = A + b + 4          # 1��1���� �ݿ����̱⶧���� day������ ��ġ�� �°� ����

    index = B % 7          # 7�� ���� �������� ���� ������ �ݺ��ǰ���
    answer = day[index]
    
    return answer

# print(solution(1,1))