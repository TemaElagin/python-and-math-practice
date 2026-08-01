# 3
# https://leetcode.com/problems/longest-substring-without-repeating-characters/description/


class Solution(object):
    def lengthOfLongestSubstring(self, s):
        seen = {}
        l = 0
        result = 0
        for i in range(len(s)):
            if s[i] not in seen:
                result = max(result,i-l+1)
            else:
                if seen[s[i]] < l:
                    result = max(result,i-l+1)
                else:
                    l = seen[s[i]] + 1
            seen[s[i]] = i
        return result
