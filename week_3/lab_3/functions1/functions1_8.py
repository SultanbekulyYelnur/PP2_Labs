def spy_game(nums):
    zeros = 0
    res = False
    for i in nums:
        if zeros >= 2 and i == 7:
            res = True
            break

        if i == 0:
            zeros += 1
        else:
            zeros = 0
     
    return res

print(spy_game([2,4,5,0,0, 7, 0, 7]))
