# 20
# https://leetcode.com/problems/valid-parentheses/description/

class Solution(object):
    def isValid(self, s):
        el_dict = {")": "(", "]": "[", "}": "{"}
        stack = []
        for el in s:
            if el in el_dict:
                top_el = stack.pop() if stack else "kakashka"
                if el_dict[el] != top_el:
                    return False
            else:
                stack.append(el)
        return not stack