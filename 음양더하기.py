def solution(absolutes, signs):
    answer = 0
    for absolute, sign in zip(absolutes, signs):
        if sign:  # sign�� True�̸� absolute���� �״�� ���Ѵ�.
            answer += absolute
        else:     # sign�� False�̸� absolute���� -�� �ٿ� ���Ѵ�.
            answer -= absolute
    return answer