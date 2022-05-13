def twoNumberSum(array, target_sum):
    # Write your code here.
    nums = {}
    for num in array:
        possible_match = target_sum-num
        if possible_match in nums:
            return [possible_match, num]
        else:
            nums[num] = True
    return []
        
twoNumberSum([3, 5, -4, 8, 11, 1, -1, 6], 10)