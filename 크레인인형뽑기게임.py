def solution(board, moves):
    stack = [] # ������ �Ű����� ��ϵ�
    cnt = 0    # ������ Ƚ��
    for col in moves:    # �̵���ġ(��)
        for i in range(len(board)):    # ���� �ִ� ��ġ�� ã��
            if board[i][col-1] != 0:
                stack.append(board[i][col-1])
                board[i][col-1] = 0
                break
        if len(stack)>1 and stack[-2] == stack[-1]:  # �������� �����ϸ� �� ���� �����ϰ� ī��Ʈ����
            del stack[-2:]
            cnt += 2
    return cnt