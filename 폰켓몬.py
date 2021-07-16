def solution(nums):
    num = len(nums) // 2 # 뽑을 수 있는 폰켓몬의 수
    nums = set(nums)  # 폰켓몬 종류 중복 제거
    if len(nums) >= num:  # 뽑을 수 있는 폰켓몬 수보다 중복제거한 폰켓몬 배열이 작을경우
        answer = num
    else:
        answer = len(nums)
    return answer