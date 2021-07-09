def solution(board, moves):
    stack = [] # 우측에 옮겨지는 블록들
    cnt = 0    # 터지는 횟수
    for col in moves:    # 이동위치(열)
        for i in range(len(board)):    # 블럭이 있는 위치를 찾음
            if board[i][col-1] != 0:
                stack.append(board[i][col-1])
                board[i][col-1] = 0
                break
        if len(stack)>1 and stack[-2] == stack[-1]:  # 이전블럭과 동일하면 두 블럭을 삭제하고 카운트증가
            del stack[-2:]
            cnt += 2
    return cnt