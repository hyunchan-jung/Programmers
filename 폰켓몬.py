def solution(nums):
    num = len(nums) // 2 # ���� �� �ִ� ���ϸ��� ��
    nums = set(nums)  # ���ϸ� ���� �ߺ� ����
    if len(nums) >= num:  # ���� �� �ִ� ���ϸ� ������ �ߺ������� ���ϸ� �迭�� �������
        answer = num
    else:
        answer = len(nums)
    return answer