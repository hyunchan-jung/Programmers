def solution(n):
    answer = 0
    if n < 3: return n
    n3 = ''
    while 1:  # 3���� ��ȯ
        n3 += str(n%3)
        if n // 3 <= 2: n3 += str(n // 3); break  # 3���� ���� ���� 2���� �۰ų� ������ ����
        else: n//=3
    a = 1
    for i in n3[::-1]:  # 3������ �Ųٷ� ���
        answer += a * int(i)
        a *= 3
    return answer