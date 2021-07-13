def solution(numbers, hand):
    Left = [1,4,7]   # 왼손으로 누르는 번호
    Right = [3,6,9]  # 오른손으로 누르는 번호
    Mid = [2,5,8,0]  # 키패드 중간에 위치한 번호

    # LR에서 1은 손이 중간라인에 위치한경우 0이된다.
    # 이동 거리 계산을 위한 값
    LR = [3,3,1,1]   # 왼손,오른손의 위치 상태
    answer = ''
    for num in numbers:
        if num in Left:  # 왼손으로 눌러야 하는 번호 1,4,7에 해당할 경우
            answer += 'L'
            LR[0] = Left.index(num)
            LR[2] = 1
        elif num in Right:
            answer += 'R'
            LR[1] = Right.index(num)
            LR[3] = 1
        else:    # 중간에 위치한 번호
            loc = Mid.index(num)  # 번호 인덱스 지정
            a = abs(LR[0]-loc)+LR[2]  # 거리계산
            b = abs(LR[1]-loc)+LR[3]  # 현재 손이 좌측 혹은 우측에 있다면 LR[3]은 1
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