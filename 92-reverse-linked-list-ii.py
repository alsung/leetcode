# Leetcode Question 92

# Given the head of a singly linked list and two integers left and right where left <= right,
# reverse the nodes of the list from position left to position right, and return the reversed
# list. 

# Example 1
# input: head = [1,2,3,4,5], left = 2, right = 4
# output: [1,4,3,2,5]

# input: head = [5], left = 1, right = 1
# output: [5]

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def reverseBetween(self, head, left, right):
        """
        :type head: ListNode
        :type left: int
        :type right: int
        :rtype: ListNode
        """
        if not head or left == right:
            return head
        
        # use dummy to ensure there is always available pre node if left = 1
        dummy = pre = ListNode(None) 
        dummy.next = head
        for i in range(left-1):
            pre = pre.next # puts pre ptr into position left - 1
        cur = pre.next # cur ptr at position left

        for i in range(right-left):
            tmp = pre.next
            pre.next = cur.next
            cur.next = cur.next.next
            pre.next.next = tmp
        return dummy.next



        