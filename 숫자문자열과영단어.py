def solution(s):
    # �� ���ڿ� ��Ī�Ǵ� ���� ��ųʸ� ����
    T = {'zero':'0', 'one':'1', 'two':'2',
        'three':'3', 'four':'4', 'five':'5',
        'six':'6', 'seven':'7', 'eight':'8',
        'nine':'9'}
    for t in T:
        s = s.replace(t, T[t]) # ��ü
    return int(s)