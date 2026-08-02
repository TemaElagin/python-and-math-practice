# 877
# https://leetcode.com/problems/stone-game/description/

class Solution(object):
    def stoneGame(self, piles):
        memory = {}
        def get_balance(left, right):
            if (left, right) in memory:
                return memory[(left, right)]

            if left == right:
                return piles[left]

            take_left = piles[left] - get_balance(left + 1, right)
            take_right = piles[right] - get_balance(left, right - 1)

            memory[(left, right)] = max(take_left, take_right)
            return memory[(left, right)]

        return get_balance(0, len(piles) - 1) >= 0



# class Solution:
#     def stoneGame(self, piles):
#         return True