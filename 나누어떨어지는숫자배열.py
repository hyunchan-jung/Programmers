def solution(arr, divisor):
    answer = []
    for i in arr:
        if i % divisor == 0:  # divisor�� ���� �������� 0�̸�
            answer.append(i)  # �迭 answer�� arr�� ��� �߰�
    if len(answer) == 0:      # answer�� ����� ���� ������
        answer.append(-1)     # -1 �߰�
    answer.sort()  # �������� ����
    return answer