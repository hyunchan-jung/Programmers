def solution(participant, completion):
    # 각 리스트 정렬
    participant.sort()
    completion.sort()
    for i in range(len(completion)):
        if completion[i] != participant[i]:  # 일치하지 않으면 participant의 i번째요소 리턴
            return participant[i]
    return participant[-1] # 일치하는 것이 없으면 참가자의 마지막요소 반환