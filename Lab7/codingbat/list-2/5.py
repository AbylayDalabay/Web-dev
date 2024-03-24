def centered_average(nums):
    snums = sorted(nums)
    sum = 0
    for i in range(1,len(nums)-2):
        sum+=snums[i]
    return sum/len(nums)-2