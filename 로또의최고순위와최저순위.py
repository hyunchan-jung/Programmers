def solution(lottos, win_nums):
    Max, Min, cnt = 0, 0, 0
    zero = 0
    for i in lottos: # ���� ���� 0�� ������ ����
        if i in win_nums:
            cnt += 1
        if i == 0:
            zero += 1
    if cnt < 2: Min = 6  # ���� ���� 2������ ������ �ּҵ���� 6��
    else: Min = [1,2,3,4,5][[6,5,4,3,2].index(cnt)]
    Max = Min - zero
    if Max == 0: Max = 1
    return [Max, Min]