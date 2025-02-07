def has_33(nums):
    threes = 0

    for i in nums:
        if threes == 2:
            break

        if i == 3:
            threes += 1
        else:
            threes = 0

    if threes == 2:
        return True
    else:
        return False



print(has_33([1,3, 3]))

