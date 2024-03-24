def big_diff(nums):
    min = 99999
    max = 0
    for num in nums:
        if(min > num): min = num
        if(max < num): max = num
    return max-min