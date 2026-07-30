# 3014
# https://leetcode.com/problems/minimum-number-of-pushes-to-type-word-i/description/?envType=daily-question&envId=2026-07-30

# Sort letters in the word from most frequent to least frequent, then the first 8 letters get a weight of 1, the next 8 get 2

class Solution(object):
    def minimumPushes(self, word):
        list_word = list(word)
        list_word.sort()

        dict_word = {}
        for el in list_word:
            if el.isalpha():
                if el in dict_word:
                    dict_word[el] += 1
                else:
                    dict_word[el] = 1

        new_list_word = [k for k, v in sorted(dict_word.items(), key=lambda x: (-x[1], x[0]))]

        i = 0
        result = 0
        for el in new_list_word:
            result += (i//8 + 1) * dict_word[el]
            i += 1
        return result

print(Solution().minimumPushes('word'))