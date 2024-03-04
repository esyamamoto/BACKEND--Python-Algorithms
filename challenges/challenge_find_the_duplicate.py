def validate(nums):
    if not nums or isinstance(nums, str):
        return False

    if len(nums) < 2:
        return False

    for num in nums:
        if not isinstance(num, int) or num < 0:
            return False
    # is too complex blablabla
    # nums.sort()

    # for i in range(len(nums) - 1):
    #    if nums[i] == nums[i + 1]:
    #       return nums[i]

    # return False
    return True


def sort_nums(nums):
    nums.sort()
    return nums


def find_duplicate(nums):
    if not validate(nums):
        return False

    nums = sort_nums(nums)

    for i in range(len(nums) - 1):
        if nums[i] == nums[i + 1]:
            return nums[i]

    return False
