def solution(s):
    # 각 숫자에 매칭되는 영어 딕셔너리 생성
    T = {'zero':'0', 'one':'1', 'two':'2',
        'three':'3', 'four':'4', 'five':'5',
        'six':'6', 'seven':'7', 'eight':'8',
        'nine':'9'}
    for t in T:
        s = s.replace(t, T[t]) # 대체
    return int(s)