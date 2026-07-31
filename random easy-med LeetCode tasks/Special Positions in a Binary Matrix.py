# 1582
#https://leetcode.com/problems/special-positions-in-a-binary-matrix/description/

#Oh no, my code is so bad(

class Solution(object):
    def numSpecial(self, mat):
        n = len(mat)
        m = len(mat[0])
        num_position = []
        for i in range(n):
            for j in range(m):
                if mat[i][j] == 1:
                    num_position.append([i, j])
        new_num_position = []
        for el in num_position:
            is_unique = 0
            for elem in num_position:
                if el[0] == elem[0] or el[1] == elem[1]:
                    is_unique += 1
            if is_unique == 1:
                new_num_position.append(el)
        return len(new_num_position)
