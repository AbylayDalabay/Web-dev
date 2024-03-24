def sum67(nums):
    six = False
    sum = 0
    seven = False
    for num in nums:
        if(six == False and seven == False) or (six and seven):
            sum+=num
    return sum
