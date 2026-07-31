# 2
# https://leetcode.com/problems/add-two-numbers/description/

# Convert lists to numbers, sum them, and make a new list

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        dummy = ListNode()
        current = dummy
        i = 0

        while l1 or l2 or i:
            v1 = l1.val if l1 else 0
            v2 = l2.val if l2 else 0

            total = v1 + v2 + i
            i = total // 10

            current.next = ListNode(total % 10)

            current = current.next
            if l1: l1 = l1.next
            if l2: l2 = l2.next

        return dummy.next

