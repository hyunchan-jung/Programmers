def solution(arr):
    answer = [arr[0]] # ù ��° ��� ����
    for i in range(1,len(arr)): # arr�� 1��° ��Һ��� �ݺ�
        if arr[i-1] != arr[i]:  # ���� ��ҿ� ���������� answer�� �߰�
            answer.append(arr[i])
    return answer