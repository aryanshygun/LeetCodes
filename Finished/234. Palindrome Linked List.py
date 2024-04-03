# https://leetcode.com/problems/palindrome-linked-list/description/?envType=daily-question&envId=2024-04-03

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        stack = []
        while head:
            stack.append(head.val)
            head = head.next
        if len(stack) <= 1:
            return True
        x = len(stack) // 2
        return stack[:x] == stack[-1:-x-1:-1]