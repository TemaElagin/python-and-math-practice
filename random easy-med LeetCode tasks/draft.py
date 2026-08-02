nums = [0,0,1,1,1,2,2,3,3,4]

new_nums = list(set(nums))
k = len(new_nums)
for _ in range(len(nums) - k):
    new_nums.append("_")
return k, new_nums