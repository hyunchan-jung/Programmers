def solution(n, lost, reserve):
    lost.sort()
    reserve.sort()
    L = lost.copy()
    for i in L:
        if i in reserve: # �� ���� �ΰ��� ü������ ������ �ְ�, �Ѱ� �н��Ѱ�� ������ ���� ü���� ���
            lost.remove(i)
            reserve.remove(i)
    L = lost.copy()
    for i in L: # �չ�ȣ ���� ��������, ������ �޹�ȣ Ž�� 
        if i-1 in reserve:
            lost.remove(i)
            reserve.remove(i-1)
        elif i+1 in reserve:
            lost.remove(i)
            reserve.remove(i+1)
    return n-len(lost)