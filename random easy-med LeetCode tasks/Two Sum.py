# 1
# https://leetcode.com/problems/two-sum/description/


#Use a hash map to find the complement

class Solution(object):
    def twoSum(self, nums, target):
        new_nums = {}
        for i in range(len(nums)):
            if target - nums[i] in new_nums:
                return [new_nums[target - nums[i]], i]
            else:
                new_nums[nums[i]] = i
        return None

print(Solution().twoSum([3, 3], 6))