def solution(numbers, hand):
    Left = [1,4,7]   # �޼����� ������ ��ȣ
    Right = [3,6,9]  # ���������� ������ ��ȣ
    Mid = [2,5,8,0]  # Ű�е� �߰��� ��ġ�� ��ȣ

    # LR���� 1�� ���� �߰����ο� ��ġ�Ѱ�� 0�̵ȴ�.
    # �̵� �Ÿ� ����� ���� ��
    LR = [3,3,1,1]   # �޼�,�������� ��ġ ����
    answer = ''
    for num in numbers:
        if num in Left:  # �޼����� ������ �ϴ� ��ȣ 1,4,7�� �ش��� ���
            answer += 'L'
            LR[0] = Left.index(num)
            LR[2] = 1
        elif num in Right:
            answer += 'R'
            LR[1] = Right.index(num)
            LR[3] = 1
        else:    # �߰��� ��ġ�� ��ȣ
            loc = Mid.index(num)  # ��ȣ �ε��� ����
            a = abs(LR[0]-loc)+LR[2]  # �Ÿ����
            b = abs(LR[1]-loc)+LR[3]  # ���� ���� ���� Ȥ�� ������ �ִٸ� LR[3]�� 1
            if a < b:
                answer += 'L'
                LR[0] = loc
                LR[2] = 0
            elif a > b:
                answer += 'R'
                LR[1] = loc
                LR[3] = 0
            else:
                if hand == 'left':
                    answer += 'L'
                    LR[0] = loc
                    LR[2] = 0
                else:
                    answer += 'R'
                    LR[1] = loc
                    LR[3] = 0
    return answer