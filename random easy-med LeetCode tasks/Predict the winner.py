# 486
#https://leetcode.com/problems/predict-the-winner/description/

class Solution(object):
    def predictTheWinner(self, nums):
        memory = {}
        def get_balance(left, right):
            if (left, right) in memory:
                return memory[(left, right)]

            if left == right:
                return nums[left]

            take_left = nums[left] - get_balance(left + 1, right)
            take_right = nums[right] - get_balance(left, right - 1)

            memory[(left, right)] = max(take_left, take_right)
            return memory[(left, right)]

        return get_balance(0, len(nums) - 1) >= 0