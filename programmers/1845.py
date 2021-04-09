def solution(nums):
    answer = 0
    set_nums = set(nums)
    answer = len(nums)//2 if len(set_nums) > len(nums)//2 else len(set_nums)

    return answer


solution([3, 1, 2, 3])
solution([3, 3, 3, 2, 2, 4])
solution([3, 3, 3, 2, 2, 2])
