# 26
# https://leetcode.com/problems/remove-duplicates-from-sorted-array/description/

class Solution(object):
    def removeDuplicates(self, nums):
        j = 0
        for i in range(len(nums)):
            if nums[i] != nums[j]:
                if j != len(nums) - 1:
                    nums[j+1] = nums[i]
                    j += 1
                else:
                    j += 1
        return j + 1