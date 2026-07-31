# 9
# https://leetcode.com/problems/palindrome-number/description/


class Solution(object):
    def isPalindrome(self, x):
        x = str(x)
        is_palindrome = True
        for i in range(len(x) // 2):
            if x[i] != x[-i - 1]:
                is_palindrome = False
        return is_palindrome