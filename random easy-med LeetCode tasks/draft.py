nums = [2,7,11,15]
target = 9

for el in nums:
    if target - el in nums:
        print(sorted([nums.index(el), nums.index(target - el)]))


