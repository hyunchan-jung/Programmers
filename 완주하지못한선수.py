def solution(participant, completion):
    # �� ����Ʈ ����
    participant.sort()
    completion.sort()
    for i in range(len(completion)):
        if completion[i] != participant[i]:  # ��ġ���� ������ participant�� i��°��� ����
            return participant[i]
    return participant[-1] # ��ġ�ϴ� ���� ������ �������� ��������� ��ȯ